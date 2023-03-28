import os
from pathlib import Path

from pydantic import BaseSettings, Field


class BaseConfig(BaseSettings):
    click_host: str = Field("localhost", env="CLICKHOUSE_HOST")
    click_port: int = Field(8123, env="CLICKHOUSE_PORT")
    service_url: str = Field("http://localhost:8001", env="UGC_SERVICE_URL")

    click_db: str = Field("shard", env="CLICKHOUSE_DB")
    click_table: str = Field("view", env="CLICKHOUSE_TABLE")

    class Config:
        env_file = os.path.join(Path(__file__).parent.absolute(), ".env")
        env_file_encoding = "utf-8"


connection_settings = BaseConfig()
