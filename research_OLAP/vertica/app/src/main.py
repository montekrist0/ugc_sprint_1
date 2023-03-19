import multiprocessing
import time
import logging

import vertica_python

from services.benchmark import BenchmarkVertica
from services.db_manager import DbManagerVertica
from core.config import settings

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

connection_info = {
    "host": settings.vertica_host,
    "port": settings.vertica_port,
    "user": settings.vertica_user,
    "password": settings.vertica_password,
    "database": settings.vertica_database,
    "autocommit": settings.vertica_autocommit,
}


def create_result_txt():
    open(settings.path_result_txt, "w").close()


def write_result_txt(lines: list[str]):
    with open(settings.path_result_txt, mode="a") as file:
        file.writelines("%s\n" % line for line in lines)


def init_process():
    with vertica_python.connect(**connection_info) as connection:
        cursor = connection.cursor()
        manager_db = DbManagerVertica(cursor)
        manager_db.init_table()
        time.sleep(2)
        manager_db.start_data_init()


def queries_in_db():
    with vertica_python.connect(**connection_info) as connection:
        cursor = connection.cursor()
        manager_db = DbManagerVertica(cursor)
        benchmark = BenchmarkVertica(manager_db)
        results = benchmark.all_requests()
        write_result_txt(results)


def load_db():
    with vertica_python.connect(**connection_info) as connection:
        cursor = connection.cursor()
        manager_db = DbManagerVertica(cursor)
        benchmark = BenchmarkVertica(manager_db)
        while True:
            benchmark.write_1000_data_in_db()


if __name__ == "__main__":
    create_result_txt()
    init_process()
    write_result_txt(["Тестирование без нагрузки"])
    queries_in_db()
    write_result_txt(["Тестирование с нагрузкой"])
    p1 = multiprocessing.Process(target=load_db)
    p2 = multiprocessing.Process(target=queries_in_db)

    p1.start()
    p2.start()

    p2.join()
    p1.terminate()
    p1.join()
