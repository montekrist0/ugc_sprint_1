import time
import multiprocessing
import vertica_python

from services.db_manager import DbManagerVertica
from services.generate_data import GeneratorFakeData
from core.config import settings

connection_info = {
    'host': settings.vertica_host,
    'port': settings.vertica_port,
    'user': settings.vertica_user,
    'password': settings.vertica_password,
    'database': settings.vertica_database,
    'autocommit': settings.vertica_autocommit,
}


def init_table():
    with vertica_python.connect(**connection_info) as connection:
        cursor = connection.cursor()
        manager_db = DbManagerVertica(cursor)
        manager_db.init_table()





def load_data(shared_var):

    with vertica_python.connect(**connection_info) as connection:
        cursor = connection.cursor()
        manager_db = DbManagerVertica(cursor)
        for _ in range(10000):
            data = GeneratorFakeData().generate(1000)
            manager_db.insert_many_data(data)
            shared_var.value += 1000

def get_data(shared_var):

    with vertica_python.connect(**connection_info) as connection:
        cursor = connection.cursor()
        manager_db = DbManagerVertica(cursor)
        cheking = (1000, 10000, 100000,1000000, 10000000)
        while True:
            if shared_var.value in cheking:
                print(shared_var, 'pussy')
                res = manager_db.count_data()
                print(res)
            print(shared_var.value)

# def test_vertica():
#
#
#     with vertica_python.connect(**connection_info) as connection:
#         cursor = connection.cursor()
#         data = GeneratorFakeData().generate(1000000)
#         print('generate is done')
#         db_manger_vertica = DbManagerVertica(cursor=cursor)
#         db_manger_vertica.insert_many_data(data)


if __name__ == "__main__":
    init_table()
    time.sleep(10)
    shared_var = multiprocessing.Value('i', 0)
    p1 = multiprocessing.Process(target=load_data, args=(shared_var,))
    p2 = multiprocessing.Process(target=get_data,args=(shared_var,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
