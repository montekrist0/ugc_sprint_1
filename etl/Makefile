up:
	make up_kafka
	make up_click_house

up_kafka:
	docker compose -f kafka.yml up -d
up_click_house:
	docker compose -f clickhouse.yml up -d
down:
	docker compose -f kafka.yml down
	docker compose -f clickhouse.yml down
del_volumes:
	docker volume prune
