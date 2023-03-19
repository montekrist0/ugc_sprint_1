from abc import ABC, abstractmethod


from brokers.kafka_broker import KafkaProducerEngine


class BaseService(ABC):
    """Базовый сервис"""

    def __init__(self, producer: KafkaProducerEngine):
        self.producer = producer

    @property
    @abstractmethod
    def topic_name(self):
        """Имя топика"""
        pass

    async def send(self, *args):
        await self.producer.send(self.topic_name, *args)
