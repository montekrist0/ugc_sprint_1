import clickhouse_connect
from flask import Flask, jsonify

# from src.services.data_generator import GeneratorFakeData
from research_OLAP.clickhouse.data_generator import GeneratorFakeData

client = clickhouse_connect.get_client(host="localhost", username="default")

data_generator = GeneratorFakeData()

app = Flask(__name__)


@app.route("/clickhouse/insert", methods=["POST"])
def clh_insert():
    client.insert(
        database="test",
        table="test",
        data=data_generator.generate(1000),
        column_names=["id", "user_id", "movie_id", "viewed_frame"],
    )

    return jsonify("ok")


@app.route("/clickhouse/select-avg")
def clh_select_avg():
    client.query("SELECT AVG(viewed_frame) FROM test.test t")
    return jsonify("ok")


@app.route("/clickhouse/select-1000")
def clh_select_all_limit_1000():
    client.query("SELECT * FROM test.test t LIMIT 1000")
    return jsonify("ok")


@app.route("/clickhouse/select-all")
def clh_select_all():
    client.query("SELECT * FROM test.test t")
    return jsonify("ok")


@app.route("/clickhouse/select-count")
def clh_select_count():
    client.query("SELECT COUNT(*) FROM test.test t")
    return jsonify("ok")


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
