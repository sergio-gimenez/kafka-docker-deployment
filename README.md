# Deploy a Kafka Broker

## A Simple Kafka Broker

First, the project provides a containerized version of it to play a bit. To deploy it, run:

```bash
docker-compose -f simple-kafka.yml up
```

**Important Caveat:** Note that by default, the broker is only (**and only**) accessible from the host machine at `localhost:29092`. To enable remote access, you should modify the `DOCKER_HOST_IP` in the `.env` file (see `.env.sample`). To properly understand what's actually going on, check [this article](https://rmoff.net/2018/08/02/kafka-listeners-explained).


## Testing the Kafka Broker

### Kafka CLI

I find handy and usefull to use the [kcat](https://github.com/edenhill/kcat#running-in-docker) tool to test the Kafka broker. The easiest and cleanest way is to use the docker image

```bash
docker run -it --network=host edenhill/kcat:1.7.1 -b '$BROKER_IP':29092 -L
```

Where `$BROKER_IP` is the IP of the host machine (the same set in `KAFKA_ADVERTISED_LISTENER`). This will list the topics available in the broker. 

If the broker is up and running, you should see something like that:

```source
Metadata for all topics (from broker -1: 192.168.200.253:29092/bootstrap):
 1 brokers:
  broker 1 at localhost:29092 (controller)
 0 topics:
```