from abc import ABC, abstractmethod

from vertica_python.vertica.cursor import Cursor


class BaseDbManager(ABC):

    @abstractmethod
    def init_table(self):
        pass

    @abstractmethod
    def insert_many_data(self, data: list[tuple]):
        pass

    @abstractmethod
    def select_data(self):
        pass

    @abstractmethod
    def count_data(self):
        pass


class DbManagerVertica(BaseDbManager):
    def __init__(self, cursor: Cursor):
        self.cursor: Cursor = cursor

    def init_table(self):
        query = '''CREATE TABLE IF NOT EXISTS views (
                        id IDENTITY,
                        user_id VARCHAR(256) NOT NULL,
                        movie_id VARCHAR(256) NOT NULL,
                        viewed_frame INTEGER NOT NULL
        );
    '''

        self.cursor.execute(query)

    def insert_many_data(self, data: list[tuple]):
        query = '''INSERT INTO views (
                        user_id,
                        movie_id,
                        viewed_frame) 
                    VALUES (?, ?, ?);'''
        self.cursor.executemany(query, data, use_prepared_statements=True)

    def select_data(self):
        query = f'SELECT * from views'
        result = self._execute(query)
        return result

    def count_data(self):
        query = f'SELECT COUNT(*) from views'
        result = self._execute(query)
        return result

    def _execute(self, query: str):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
