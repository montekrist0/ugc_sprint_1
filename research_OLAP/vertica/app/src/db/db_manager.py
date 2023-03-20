from abc import ABC, abstractmethod

import backoff

from vertica_python.vertica.cursor import Cursor
from vertica_python.errors import ConnectionError

from db.queries import Queries


class BaseDbManager(ABC):
    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_start_data(self):
        pass

    @abstractmethod
    def write_data(self, query: str, data: list[tuple]):
        pass

    @abstractmethod
    def get_data(self, query: str):
        pass


class DbManagerVertica(BaseDbManager):
    def __init__(self, cursor: Cursor):
        self.cursor: Cursor = cursor

    @backoff.on_exception(backoff.expo, ConnectionError, max_tries=10)
    def create_table(self):
        self.cursor.execute(Queries.create_table.value)

    @backoff.on_exception(backoff.expo, Exception, max_tries=5)
    def create_start_data(self):
        self.cursor.execute(Queries.create_start_data.value)

    @backoff.on_exception(backoff.expo, Exception, max_tries=5)
    def write_data(self, query: str, data: list[tuple]):
        self.cursor.executemany(query, data, use_prepared_statements=True)

    @backoff.on_exception(backoff.expo, Exception, max_tries=5)
    def get_data(self, query: str):
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result
