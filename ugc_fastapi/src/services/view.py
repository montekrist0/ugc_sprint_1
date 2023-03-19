from functools import lru_cache

from fastapi import Depends

from services.base_service import BaseService
from brokers.kafka_broker import KafkaProducerEngine, get_kafka_broker


class ViewService(BaseService):
    """Класс движка для отправки сообщений в соответствующий топик Kafka"""

    topic_name = "view"


@lru_cache()
def get_view_service(producer: KafkaProducerEngine = Depends(get_kafka_broker),) -> ViewService:
    return ViewService(producer)
