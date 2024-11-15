import flask
import redis
from flask.typing import ResponseReturnValue

redis_client = redis.Redis(host="localhost", port=6379, db=0)
app = flask.Flask(__name__)


@app.route("/unique_ip_count", methods=["GET"])
def get_unique_ip_count() -> ResponseReturnValue:
    unique_count = redis_client.pfcount("unique_device_ips")
    return flask.jsonify({"unique_device_ip_count": unique_count})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
