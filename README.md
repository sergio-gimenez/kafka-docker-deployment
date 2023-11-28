# Deploy a Kafka Broker

## A Simple Kafka Broker

First, the project provides a containerized version of it to play a bit. To deploy it, run:

```bash
docker-compose -f simple-kafka.yml up
```

**Important Caveat:** Note that by default, the broker is only (and only) accessible from the host machine at `localhost:29092`. To enable remote access, you should modify the `KAFKA_ADVERTISED_LISTENERS` environment variable in the `docker-compose.yml` file. More info in [this article](https://rmoff.net/2018/08/02/kafka-listeners-explained).

## Full Stack Kafka Broker

A full stack Kafka broker is provided. It is based on the [conduktor/kafka-stack-docker-compose](https://github.com/conduktor/kafka-stack-docker-compose). Before running it, note that the `DOCKER_HOST_IP` environment variable should be set to the IP of the host machine. A convinient way to do that is to create a `.env` file in the `tests/kafka_server_mock` folder with the following content:

```bash
DOCKER_HOST_IP=X.X.X.X
```

Now, to deploy it, run:

```bash
docker-compose -f kafka-full-stack.yml up
```

Wait a bit and a nice GUI for Kafka will be available at `$DOCKER_HOST_IP:8080`.

## Testing the Kafka Broker

To test the Kafka broker, you can use the `kafka_server_mock.py` script. It is a simple script that uses the `kafka-python` library to send and receive messages from the broker. To run it, first install the dependencies:

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then, run the script:

```bash
python -m unittest test_kafka_consumer_producer.py
```
