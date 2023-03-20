import csv
import logging
import time

from faker import Faker

TOTAL_AMOUNT = 10_000_000
BATCH_SIZE = 1000


class GeneratorFakeData:
    def __init__(self):
        self.faker = Faker()

    def generate(self, quantity: int = 100) -> list[tuple]:
        return [
            (self.faker.uuid4(), self.faker.uuid4(), self.faker.uuid4(), self.faker.random_int(min=0, max=180))
            for _ in range(quantity)
        ]


def write_rows_to_file(total_count: int = 100_000, batch_size: int = 10_000_00):
    with open("data.csv", mode="w") as file:
        writer = csv.writer(file)
        headers = ["id", "user_id", "movie_id", "viewed_frame"]
        writer.writerow(headers)

        for _ in range(1, total_count, batch_size):
            writer.writerows(gf.generate(batch_size))


if __name__ == "__main__":
    gf = GeneratorFakeData()

    start = time.monotonic()
    write_rows_to_file(total_count=TOTAL_AMOUNT, batch_size=BATCH_SIZE)
    logging.info("Время создания CSV-файла с 10 миллионами файлов - %s", time.monotonic() - start)
