import asyncio
import logging
from typing import Optional

from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError

from .base_broker import BaseProducerEngine
from core.configs import KafkaConfig, kafka_config
from datetime import datetime
import json

logger = logging.getLogger(__name__)


class KafkaProducerEngine(BaseProducerEngine):
    """Класс брокера сообщений Apache Kafka"""

    def __init__(self, producer: AIOKafkaProducer):
        self.producer = producer

    async def send(self, topic_name: str, film_id: str, user_id: str, value: int):

        value = {
            'user_id': user_id,
            'film_id': film_id,
            'viewed_frame': value,
            'event_time': str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}

        try:
            key = f'{film_id}:{user_id}'.encode('utf-8')
            await self.producer.send(
                topic=topic_name,
                value=json.dumps(value, ensure_ascii=False).encode('utf-8'),
                key=key,
            )
        except KafkaError as ex:
            logger.exception(f"Producer не смог отправить событие. Ошибка: {ex}")


kafka_broker: Optional[KafkaProducerEngine] = None


async def get_kafka_broker():
    return kafka_broker


def get_kafka_producer():

    loop = asyncio.get_event_loop()
    return AIOKafkaProducer(loop=loop,
                            bootstrap_servers=f'{kafka_config.kafka_host}:{kafka_config.kafka_port}')
