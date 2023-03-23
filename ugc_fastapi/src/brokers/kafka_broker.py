import asyncio
import logging
from typing import Optional

from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError

from .base_broker import BaseProducerEngine
from core.configs import KafkaConfig, kafka_config

logger = logging.getLogger(__name__)


class KafkaProducerEngine(BaseProducerEngine):
    """Класс брокера сообщений Apache Kafka"""

    def __init__(self, producer: AIOKafkaProducer):
        self.producer = producer

    async def send(self, topic_name: str, film_id: str, user_id: str, value: str):
        try:
            key = f'{film_id}:{user_id}'.encode()
            await self.producer.send(
                topic=topic_name,
                value=value.encode(),
                key=key,
            )
        except KafkaError as ex:
            logger.exception(f"Producer не смог отправить событие. Ошибка: {ex}")


kafka_broker: Optional[KafkaProducerEngine] = None


async def get_kafka_broker():
    global kafka_broker
    if not kafka_broker:
        loop = asyncio.get_event_loop()

        kafka_producer = AIOKafkaProducer(loop=loop,
                                          bootstrap_servers=f'{kafka_config.KAFKA_HOST}:{kafka_config.KAFKA_PORT}')
        await kafka_producer.start()
        kafka_broker = KafkaProducerEngine(producer=kafka_producer)

    return kafka_broker
