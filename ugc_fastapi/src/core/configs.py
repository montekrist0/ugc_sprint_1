import os
from typing import Union, List

from pydantic import BaseSettings
from pydantic.fields import Field

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BaseConfig(BaseSettings):

    class Config:
        env_file = os.path.join(BASE_DIR, '../.env')
        env_file_encoding = 'utf-8'


class KafkaConfig(BaseConfig):
    """Конфигурация кафки"""

    KAFKA_HOST: str = Field(env='KAFKA_HOST')
    KAFKA_PORT: int = Field(env='KAFKA_PORT')


kafka_config = KafkaConfig()
