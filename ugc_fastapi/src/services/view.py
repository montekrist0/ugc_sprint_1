from functools import lru_cache

from fastapi import Depends

from services.base_service import BaseService
from brokers.kafka_broker import KafkaProducerEngine, get_kafka_broker
from core.configs import kafka_config


class ViewService(BaseService):
    """Класс движка для отправки сообщений в соответствующий топик Kafka"""

    topic_name = kafka_config.kafka_topic_name

    async def send(self, *args):
        await self.producer.send(self.topic_name, *args)


@lru_cache()
def get_view_service(
    producer: KafkaProducerEngine = Depends(get_kafka_broker),
) -> ViewService:
    return ViewService(producer)
