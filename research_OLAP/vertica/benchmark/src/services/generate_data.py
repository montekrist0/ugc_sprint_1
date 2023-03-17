from faker import Faker


class GeneratorFakeData:
    def __init__(self):
        self.faker = Faker()

    def __del__(self):
        del self.faker

    def generate(self, quantity: int) -> list[tuple]:
        data = []
        for _ in range(quantity):
            data.append(
                (
                    self.faker.uuid4(),
                    self.faker.uuid4(),
                    self.faker.random_int(min=0, max=180)
                )
            )
        return data


asd = GeneratorFakeData().generate(4)
print(asd)