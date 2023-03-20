CREATE DATABASE IF NOT EXISTS test;

CREATE TABLE test.test (
    id String,
    user_id String,
    movie_id String,
    viewed_frame Int16
)
ENGINE = MergeTree()
ORDER BY viewed_frame;

SET input_format_csv_skip_first_lines = 1;
INSERT INTO test.test FROM INFILE 'data.csv' FORMAT CSV;