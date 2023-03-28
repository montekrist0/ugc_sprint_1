from http import HTTPStatus
from requests import post
from tests.functional.settings import connection_settings
import time

test_url = f"{connection_settings.service_url}/api/v1/test_film_id/view_progress"


def test_success_send_to_kafka():
    """
    Описание: Сервис UGC должен возвращать статус 200 при успешной передаче времени просмотра фильма.
    """
    test_data = {"film_id": "id3", "user_id": "id2", "value": 1}
    response = post(url=test_url, json=test_data)

    assert response.status_code == HTTPStatus.OK


def test_success_send_1000_rows_to_kafka(clickhouse_client):
    """
    Описание: вставка total_insert строк и проверка того, что все 1к строк попали в ClickHouse.
    """
    total_insert = 100

    query = f"SELECT COUNT(*) as count FROM {connection_settings.click_db}.{connection_settings.click_table}"

    start_count_rows = clickhouse_client.query(query).first_item.get("count")

    for i in range(1, total_insert):
        data = {"film_id": "test_film_id", "user_id": "test_user_id", "value": i}
        post(url=test_url, json=data)

    # sleep before data gets to clickhouse table
    time.sleep(10)
    count_rows_after_insert = clickhouse_client.query(query).first_item.get("count")

    assert (count_rows_after_insert - start_count_rows) == total_insert


def test_invalid_json_body_send_to_kafka():
    """
    Описание: Сервис UGC должен возвращать ошибку 422 при передаче некорректного тела запроса.
    """
    test_incorrect_data = {"film_id": "id3", "user_id": "id2", "incorrect_field": 1}
    response = post(url=test_url, json=test_incorrect_data)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
