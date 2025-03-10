from aiokafka import AIOKafkaProducer
import asyncio
import json

KAFKA_BROKER = "kafka:9092"
TOPIC_NAME = "test-topic"

async def send_message(message: dict):
    print("🚀 Kafka Producer: Connecting to Kafka...") 
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    
    await producer.start()
    print("✅ Kafka Producer: Connected!")
    
    try:
        print(f"📤 Sending message: {message}") 
        await producer.send_and_wait(TOPIC_NAME, message)
        print("✅ Message sent!")
    except Exception as e:
        print(f"❌ Kafka Error: {e}")
    finally:
        print("🔄 Closing Kafka Producer...")
        await producer.stop()
        print("✅ Kafka Producer Closed.")
