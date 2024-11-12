# lumu-backend-test
Repository holding Lumu Python Backend Test

# How to Use
In order to run Part 2, Redis and Kafka must be installed on the machine. Once these components are up and running, follow the steps below.

## Create a Virtual Environment and Install Dependencies: 
Create and activate the virtual environment:

```shell
python3 -m venv lumu-test
source lumu-test/bin/activate
```

Next, install the dependencies listed in the requirements file:

```shell
pip install -r requirements.txt
```

## Run the consumer
The consumer is located in the file `source/part_2/part_2_redis.py`. This script connects to the Redis instance and also creates the Kafka consumer. The only required argument is the Kafka topic, but the Kafka server and Redis port are also valid arguments

Start the consumer with the following command:
```shell
python3 source/part_2/part_2_redis.py
```

## Run the producer
The producer script is located in  `source/part_2/producer.py`. This code, provided by Lumu, simulates the constant flow of incoming messages.

Start the producer with the following command:
```shell
python3 source/part_2/part_2_redis.py
```

## Query the API.
To check the current count of unique IP addresses, an API endpoint is available by running the visualizer.

Start the visualizer with the following command:
```shell
python3 source/part_2/part_2_visualizer.py
```

To query the current count, use the following `curl` command (assuming the default localhost and port `5001`):
```shell
curl localhost:5001/unique_ip_count
```

This will return a JSON response containing the current unique IP count:
```json
{"unique_device_ip_count":592}
```

# Summary

## Explanation of Implementation and Scalability Challenges
This implementation will handle incoming messages in a distributed manner by allowing each node to consume messages from Kafka and increment the unique IP count in Redis.

- Kafka Consumer Group: Each node joins the same Kafka consumer group (unique_ip_counter_group), so Kafka will distribute the messages among the nodes in this group, allowing for horizontal scaling.
- Redis HyperLogLog: Using `pfadd` and `pfcount` with Redis allows us to maintain an approximate unique IP count in a memory-efficient manner, even with large volumes of data.
- REST API: The API endpoint can run on any node, allowing us to query the current count from the centralized Redis HyperLogLog.
  
## Scalability Challenges
- Redis Centralization: If there’s high contention, a Redis cluster or sharded Redis instances may be required.
- Data Consistency: Network issues could cause some nodes to lose connectivity with Redis. To mitigate this, retry logic or Kafka’s persistence features can be added to replay missed messages.
- Load Balancing for API Requests: If multiple external systems query the REST API, a load balancer in front of the nodes could help distribute the requests evenly across nodes.
