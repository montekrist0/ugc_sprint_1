

import uvicorn
from fastapi import FastAPI

from api.v1 import view_progress
from brokers import kafka_broker

app = FastAPI(
    title='API для взаимодействия с брокером сообщений',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    description='Сообщения о времени остановки просмотра фильма',
    version='1.0.0'
)


app.include_router(view_progress.router, prefix='/api/v1')


@app.on_event('startup')
async def startup():

    kafka_producer = kafka_broker.get_kafka_producer()
    await kafka_producer.start()

    kafka_broker.kafka_broker = kafka_broker.KafkaProducerEngine(producer=kafka_producer)


@app.on_event('shutdown')
async def shutdown():
    await kafka_broker.kafka_broker.producer.stop()


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8001,
        reload=True
    )
