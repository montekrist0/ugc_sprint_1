import os

from pydantic import BaseSettings
from pydantic.fields import Field

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ProducerError(Exception):
    pass


class BaseConfig(BaseSettings):
    class Config:
        env_file = os.path.join(BASE_DIR, "../../.env")
        env_file_encoding = "utf-8"


class KafkaConfig(BaseConfig):
    """Конфигурация кафки"""

    kafka_host: str = Field(env="KAFKA_HOST")
    kafka_port: int = Field(env="KAFKA_PORT")
    kafka_topic_name: str = Field(env="KAFKA_TOPIC_NAME")


kafka_config = KafkaConfig()
