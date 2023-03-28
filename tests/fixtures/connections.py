import pytest

from tests.functional.settings import connection_settings
import clickhouse_connect


@pytest.fixture(scope="session")
def clickhouse_client():
    client = clickhouse_connect.get_client(host=connection_settings.click_host, username="default")
    yield client
    client.close()
