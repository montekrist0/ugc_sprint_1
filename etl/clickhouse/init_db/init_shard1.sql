CREATE DATABASE IF NOT EXISTS shard;
CREATE DATABASE IF NOT EXISTS replica;

CREATE TABLE IF NOT EXISTS shard.kafka_film_timestamp (
      user_id String,
      film_id String,
      viewed_frame Int16,
      event_time DateTime('Europe/Moscow'))
      ENGINE = Kafka
      SETTINGS kafka_broker_list = 'broker:29092',
               kafka_topic_list = 'films-timestamps',
               kafka_group_name = 'timestamp-viewers-group',
               kafka_format = 'JSONEachRow',
               kafka_commit_every_batch = 1,
               kafka_num_consumers = 3,
               kafka_max_block_size = 10000,
               kafka_poll_max_batch_size = 10000,
               kafka_thread_per_consumer = 1,
               kafka_handle_error_mode = 'stream';


CREATE MATERIALIZED VIEW IF NOT EXISTS consumer TO shard.film_timestamp
      AS SELECT * FROM  shard.kafka_film_timestamp;

CREATE TABLE IF NOT EXISTS shard.film_timestamp (
      user_id String,
      film_id String,
      viewed_frame Int16,
      event_time DateTime('Europe/Moscow'))
      Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/film_timestamp', 'replica_1') PARTITION BY toYYYYMMDD(event_time) ORDER BY user_id;

CREATE TABLE IF NOT EXISTS replica.film_timestamp (
      user_id String,
      film_id String,
      viewed_frame Int16,
      event_time DateTime('Europe/Moscow'))
      Engine=ReplicatedMergeTree('/clickhouse/tables/shard2/film_timestamp', 'replica_2') PARTITION BY toYYYYMMDD(event_time) ORDER BY user_id;

CREATE TABLE IF NOT EXISTS default.film_timestamp (
      user_id String,
      film_id String,
      viewed_frame Int16,
      event_time DateTime('Europe/Moscow'))
      ENGINE = Distributed('company_cluster', '', film_timestamp, rand());