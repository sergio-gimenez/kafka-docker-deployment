import unittest
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError

# Kafka broker configuration
bootstrap_servers = '192.168.10.255:9092'
topic = 'my_topic'


class TestKafka(unittest.TestCase):

    def test_produce_message(self):
        # Produce a message to the topic
        print("Creating Kafka producer instance...")
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        message = "Hello, Kafka!"
        future = producer.send(topic, message.encode('utf-8'))
        # Wait for the message to be sent
        result = future.get(timeout=10)
        print("Message '{}' sent successfully!".format(message))
        producer.close()
        self.assertIsNotNone(result)

    def test_consume_message(self):
        # Create Kafka consumer instance
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
        )

        # Consume the message
        message = next(consumer)
        self.assertIsNotNone(message)
        self.assertEqual(message.value.decode('utf-8'), "Hello, Kafka!")
        print("Message '{}' consumed successfully!".format(
            message.value.decode('utf-8')))

        # Close the consumer gracefully
        consumer.close()


if __name__ == '__main__':
    unittest.main()
