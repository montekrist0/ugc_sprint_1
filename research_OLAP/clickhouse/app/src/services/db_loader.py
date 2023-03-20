import time

import clickhouse_connect

from research_OLAP.clickhouse.data_generator import GeneratorFakeData

SLEEP_TIME_BETWEEN_INSERT = 0.05


def main():
    data_generator = GeneratorFakeData()
    client = clickhouse_connect.get_client(host="localhost", username="default")

    while True:
        client.insert(
            database="test",
            table="test",
            data=data_generator.generate(1000),
            column_names=["id", "user_id", "movie_id", "viewed_frame"],
        )
        time.sleep(SLEEP_TIME_BETWEEN_INSERT)


if __name__ == "__main__":
    main()
