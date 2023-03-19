

from kafka import KafkaConsumer

SERVER = 'localhost:9092'

TOPIC1 = 'recorder1'
TOPIC2 = 'recorder2'

if __name__ == "__main__":
    print("Starting producer...")

    consumer = KafkaConsumer(
        bootstrap_servers=[SERVER]
    )

    consumer.subscribe(TOPIC1)

    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))