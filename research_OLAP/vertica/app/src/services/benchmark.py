import time

from services.db_manager import DbManagerVertica
from services.generate_data import generator_data


class BenchmarkVertica:
    def __init__(self, db_manager: DbManagerVertica):
        self.db_manager = db_manager
        self.generator_data = generator_data

    def all_requests(self):
        result_base = self.base_requests()
        result_agr = self.agr_request()
        return result_agr + result_base

    def base_requests(self):
        results = []
        time_insert = self.insert_1000_data()
        result_insert = f"Время вставки 1000 данных составило {time_insert} сек."
        time_select_all = self.select_all_data()
        result_select_all = (
            f"Время получения всех данных составило {time_select_all} сек."
        )
        results.append(result_insert)
        results.append(result_select_all)
        return results

    def agr_request(self):
        results = []
        time_avg = self.avg_data()
        result_avg = (
            f'Время подсчета "среднего просмотра фильма" составило {time_avg} сек.'
        )
        time_count = self.count_data()
        result_count = f"Время подсчета кол-во данных составило {time_count} сек."
        results.append(result_avg)
        results.append(result_count)
        return results

    def avg_data(self):
        start_time = time.monotonic()
        self.db_manager.avg_data()
        end_time = time.monotonic() - start_time
        return end_time

    def count_data(self):
        start_time = time.monotonic()
        self.db_manager.count_data()
        end_time = time.monotonic() - start_time
        return end_time

    def load_start_data(self):
        self.db_manager.start_data_init()

    def insert_1000_data(self):
        time_write = self.write_1000_data_in_db()
        return time_write

    def write_1000_data_in_db(self):
        data = self.generator_data.generate(1000)
        start_time = time.monotonic()
        self.db_manager.insert_many_data(data)
        end_time = time.monotonic() - start_time
        return end_time

    def select_all_data(self):
        start_time = time.monotonic()
        self.db_manager.select_all_data()
        end_time = time.monotonic() - start_time
        return end_time
