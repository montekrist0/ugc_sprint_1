# UGC-спринт

## 1 Назначение модуля:

Данный модуль является частью проекта "Онлайн-кинотеатр", в которой представлена **асинхронная реализация API** для получения информации
о просмотре фильмов (какой пользователь, на каком фильме, на каком моменте фильма остановился).

В сервисе реализован ETL-процесс.

---

## 2 Используемые технологии сервиса

Технологический стек проекта:

1. [Kafka](https://kafka.apache.org) — распределённый программный брокер сообщений;
2. [Clickhouse](https://clickhouse.com) — колоночная аналитическая СУБД для хранения контента, генерируемого пользователями;
3. [Zookeper](https://zookeeper.apache.org) — открытая программная служба для координации распределённых систем
4. [Nginx](https://www.nginx.com/) — веб-сервер;
5. FastAPI — веб-фреймворк для создания API, написанный на Python. Используется для реализации API
для получения информации и дальнейшей отправки в кафку данных о просмотре фильма; 
6. ETL-процесс, реализованный с использованием FastAPI и _kafka table engine_ (движок таблицы Clickhouse, позволяющий
получать сообщения из топиков Kafka);

Каждый модуль (сервис) запускается с помощью [Docker](https://www.docker.com/) контейнеров, тем самым реализуя в проекте микросервисную архитектуру.
Сервисы связаны между собой с помощью `docker compose`.

---

## 3 Запуск проекта

Для запуска проекта достаточно:
1. Убедиться, что в корне репозитория имеется файл `.env` с введенными параметрами по примеру `.env.example`;
2. Выполнить команду `docker compose up`

___
## 4 Описание API

Для передачи данных о просмотре фильма необходимо выполнить POST-запрос по адресу:
`https://localhost:443/api/v1/{film_id}/view_progress` с `Content-Type: application/json` и телом запроса вида:
```json lines
{
    "film_id": "id3",
    "user_id": "id2",
    "value": 1
}
```
