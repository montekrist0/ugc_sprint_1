from abc import ABC, abstractmethod

import backoff

from vertica_python.vertica.cursor import Cursor
from vertica_python.errors import ConnectionError


class BaseDbManager(ABC):
    @abstractmethod
    def init_table(self):
        pass

    @abstractmethod
    def insert_many_data(self, data: list[tuple]):
        pass

    @abstractmethod
    def count_data(self):
        pass


class DbManagerVertica(BaseDbManager):
    def __init__(self, cursor: Cursor):
        self.cursor: Cursor = cursor

    @backoff.on_exception(backoff.expo, ConnectionError, max_tries=5)
    def init_table(self):
        query = """CREATE TABLE IF NOT EXISTS views (
                        id IDENTITY,
                        user_id VARCHAR(256) NOT NULL,
                        movie_id VARCHAR(256) NOT NULL,
                        viewed_frame INTEGER NOT NULL
        );
    """

        self.cursor.execute(query)

    @backoff.on_exception(backoff.expo, Exception, max_tries=5)
    def start_data_init(self):
        query = "COPY views(user_id, movie_id, viewed_frame) FROM '/fish_data.csv' DELIMITER ','"
        self.cursor.execute(query)

    @backoff.on_exception(backoff.expo, Exception, max_tries=5)
    def insert_many_data(self, data: list[tuple]):
        query = """INSERT INTO views (
                        user_id,
                        movie_id,
                        viewed_frame) 
                    VALUES (?, ?, ?);"""
        self.cursor.executemany(query, data, use_prepared_statements=True)

    @backoff.on_exception(backoff.expo, Exception, max_tries=5)
    def count_data(self):
        query = f"SELECT COUNT(*) from views"
        result = self._execute(query)
        return result

    @backoff.on_exception(backoff.expo, Exception, max_tries=5)
    def avg_data(self):
        query = f"SELECT AVG(viewed_frame) from views"
        result = self._execute(query)
        return result

    @backoff.on_exception(backoff.expo, Exception, max_tries=5)
    def select_all_data(self):
        query = f"SELECT * from views"
        result = self._execute(query)
        return result

    @backoff.on_exception(backoff.expo, Exception, max_tries=5)
    def _execute(self, query: str):
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result
