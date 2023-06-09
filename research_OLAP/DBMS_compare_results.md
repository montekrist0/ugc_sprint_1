# Результаты сравнения хранилищ Vertica и ClickHouse

## 1 Виды тестов

Тесты проходят как под нагрузкой(периодическая запись 1000 строк), так и без нагрузки
Предварительно в обе БД загружаются через .csv файл 10 млн записей.

После загрузки данных происходят тесты:
  - На получение всех строк
  - На получение 1000 строк
  - На вставку 1000 строк
  - На подсчет AVG viewed_frame
  - На подсчет количества строк 


## 2 Результаты тестов

### 2.1 Без нагрузки

|                              | Clickhouse | Vertica |
|------------------------------|:----------:|:-------:|
| Получение 1к строк           |   114 мс   |    -    |
| Получение всех строк         |    33 с    |  20 с   |
| Вставка 1к строк             |   10 мс    | 14.6 с  |
| Подсчет AVG по одной колонке |   12 мс    | 57.7 с  |
| Подсчет количества строк     |    8 мс    | 110 мс  |


### 2.2 С нагрузкой

|                              | Clickhouse | Vertica |
|------------------------------|:----------:|:-------:|
| Получение 1к строк           |   118 мс   |    -    |
| Получение всех строк         |     -      | 20.9 с  |
| Вставка 1к строк             |   11 мс    | 11.2 с  |
| Подсчет AVG по одной колонке |   13 мс    | 59.3 с  |
| Подсчет количества строк     |    7 мс    | 112 мс  |


## Выводы

Clickhouse показал себя более производительной СУБД. 
Такимо образом, в качестве OLAP-хранилища выбран Clickhouse.