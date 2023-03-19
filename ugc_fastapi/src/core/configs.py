import os
from typing import Union, List

from pydantic import BaseSettings
from pydantic.fields import Field

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BaseConfig(BaseSettings):

    class Config:
        env_file = os.path.join(BASE_DIR, '../../.env.local')
        env_file_encoding = 'utf-8'


# class LogConfig(BaseConfig):
#
#     CONSOLE_LOG_LEVEL: str = Field(env='CONSOLE_LOG_LEVEL')
#     UVICORN_LOG_LEVEL: str = Field(env='UVICORN_LOG_LEVEL')
#     ROOT_LOG_LEVEL: str = Field(env='ROOT_LOG_LEVEL')


class KafkaConfig(BaseSettings):
    """Represents the configuration for the Kafka client."""

    class Config:
        env_prefix = "KAFKA_"

    bootstrap_servers: Union[List[str], str] = 'localhost:9092'


kafka_config = KafkaConfig()
