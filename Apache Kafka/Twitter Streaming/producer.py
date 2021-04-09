from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Sending test events
producer.send('sample', b'Hello!')
producer.send('sample', key=b'message-two', value=b'Kafka in use!')
producer.flush()