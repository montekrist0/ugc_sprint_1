import random
from faker import Faker
from kafka import KafkaProducer
from time import sleep
import pickle
import datetime
import json

# data = {'user_id': 'qwe', 'film_id': 'qwe', 'viewed_frame': random.randint(0, 180),
#         'event_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode('utf-8'))

faker = Faker()
# dates = []
# keys = []
for _ in range(100):
    year = 2022
    month = 5
    day = 24
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    random_date = datetime.datetime(year, month, day, hour, minute, second)
    formatted_date = random_date.strftime('%Y-%m-%d %H:%M:%S')
    data = {'user_id': str(faker.uuid4()), 'film_id': str(faker.uuid4()), 'viewed_frame': random.randint(0, 180),
            'event_time': formatted_date}


    b = f'{data["user_id"]}+{data["film_id"]}'
    c = pickle.dumps(b)
    producer.send(
        'view',
        value=data,
        key=c,
    )
    sleep(0.2)
#     dates.append(data)
#     keys.append(c)
#
#
# for index, value in enumerate(dates):
#     producer.send(
#         'films-timestamps',
#         value=value,
#         key=keys[index],
#     )

