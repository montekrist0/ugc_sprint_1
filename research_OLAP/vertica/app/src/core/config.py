from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    vertica_host: str = Field(default="127.0.0.1", env="VERTICA_HOST")
    vertica_port: int = Field(default=5433, env="VERTICA_PORT")
    vertica_user: str = Field(default="dbadmin", env="VERTICA_USER")
    vertica_password: str = Field(default="", env="VERTICA_PASSWORD")
    vertica_database: str = Field(default="docker", env="VERTICA_DATABASE")
    vertica_autocommit: bool = Field(default=True, env="VERTICA_AUTOCOMMIT")
    path_result_txt: str = Field(default="./result_vertica.txt", env="PATH_RESULT_TXT")


settings = Settings()
