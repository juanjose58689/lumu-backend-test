import argparse
import json
import threading

import redis
from kafka import KafkaConsumer  # type: ignore

parser = argparse.ArgumentParser(description="Kafka Message Sender")
parser.add_argument("--topic", required=True, help="Kafka topic to send messages to")
parser.add_argument(
    "--bootstrap_servers", default="localhost:9092", help="Kafka bootstrap servers"
)
parser.add_argument(
    "--redis_port", default=6379, type=int, help="Kafka bootstrap servers"
)
args = parser.parse_args()

redis_client = redis.Redis(host="localhost", port=args.redis_port, db=0)

consumer = KafkaConsumer(
    args.topic,
    bootstrap_servers=[args.bootstrap_servers],
    group_id="unique_ip_counter_group",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
)


def process_message(message: dict) -> None:
    """Process a message to extract the IP address."""
    if device_ip := message.get("device_ip"):
        redis_client.pfadd("unique_device_ips", device_ip)


def consume_messages() -> None:
    """Consume messages from Kafka and process each one."""
    for msg in consumer:
        process_message(msg.value)


consumer_thread = threading.Thread(target=consume_messages)
consumer_thread.daemon = True
consumer_thread.start()
consumer_thread.join()
