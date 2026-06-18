import json
import random
import time
from datetime import datetime
from uuid import uuid4

from faker import Faker
from kafka import KafkaProducer

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

products = ["Laptop", "Phone", "Headphones", "Keyboard", "Mouse", "Monitor"]
payment_methods = ["card", "cash", "wallet"]
payment_statuses = ["paid", "failed", "pending"]


def generate_order():
    return {
        "order_id": str(uuid4()),
        "customer_id": f"CUST-{random.randint(1, 100)}",
        "customer_name": fake.name(),
        "product": random.choice(products),
        "quantity": random.randint(1, 5),
        "amount": round(random.uniform(100, 50000), 2),
        "payment_method": random.choice(payment_methods),
        "payment_status": random.choice(payment_statuses),
        "event_time": datetime.utcnow().isoformat()
    }


while True:
    order = generate_order()
    producer.send("orders", value=order)
    producer.flush()

    print(f"Sent order: {order}")

    time.sleep(2)