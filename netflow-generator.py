import json, time, random
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    data = {"src_ip": f"192.168.0.{random.randint(1,255)}",
            "dst_ip": f"10.0.0.{random.randint(1,255)}",
            "bytes": random.randint(100,10000)}
    producer.send('netflow', data)
    print("Produced:", data)
    time.sleep(1)
