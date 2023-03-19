from kafka import KafkaProducer

SERVER = 'localhost:9092'

TOPIC1 = 'recorder1'
TOPIC2 = 'recorder2'

def partitioner(serialized_key, all_partitions, available_partitions):
    key = int(serialized_key)
    return key % 2

if __name__ == "__main__":
    print("Starting producer...")

    producer = KafkaProducer(
        bootstrap_servers=SERVER,
        partitioner=partitioner,
        max_in_flight_requests_per_connection=1,
    )
    c = 0

    for i in range(10):
        message = f'Message number {i}'

        producer.send(
            TOPIC1,
            key=bytes(str(i), 'utf-8'),
            value=bytes(message, 'utf-8'),
        )

        c = c + 1 if c else c - 1
    
    print(producer.partitions_for("recorder1"))
    producer.flush()