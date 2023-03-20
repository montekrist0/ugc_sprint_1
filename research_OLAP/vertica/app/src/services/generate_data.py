from faker import Faker


class GeneratorFakeData:
    def __init__(self):
        self.faker = Faker()

    def generate(self, quantity: int) -> list[tuple]:
        return [
            (self.faker.uuid4(), self.faker.uuid4(), self.faker.random_int(min=0, max=180)) for _ in range(quantity)
        ]


generator_data = GeneratorFakeData()
