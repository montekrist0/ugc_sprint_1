import csv
from faker import Faker


class GeneratorFakeData:
    def __init__(self):
        self.faker = Faker()

    def generate(self, quantity: int) -> list[tuple]:
        data = []
        for _ in range(quantity):
            data.append(
                (
                    self.faker.uuid4(),
                    self.faker.uuid4(),
                    self.faker.random_int(min=0, max=180),
                )
            )
        return data


if __name__ == "__main__":
    gen_fish_data = GeneratorFakeData()

    data = gen_fish_data.generate(10000000)

    with open('fish_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
