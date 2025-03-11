
from aiokafka import AIOKafkaConsumer
import asyncio
import json
from service.db_service import PostgresDBService
from model.database import get_db

KAFKA_BROKER = "kafka:9092"
TOPIC_NAME = "test-topic"

async def consume():
    try:
        print("🚀 Kafka Consumer: Connecting to Kafka...") 

        consumer = AIOKafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=KAFKA_BROKER,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            group_id="my-group", 
            auto_offset_reset="earliest"
        )

        await consumer.start()
        print("✅ Kafka Consumer: Connected and Listening!")

        async for msg in consumer:
            data = msg.value
            db_session = await get_db().__anext__()  
            if data["event"] == "task_created":
                await PostgresDBService.create_task(db_session, data["data"])
                await db_session.commit() 
                print(f"📥 Task saved: {data['data']}")

            elif data["event"] == "task_updated":
                task = await PostgresDBService.get_task(db_session, data["data"]["id"])
                if task:
                    await PostgresDBService.update_task(db_session, task, data["data"])
                    await db_session.commit()
                    print(f"📝 Task updated: {data['data']}")
                else:
                    print(f"❌ Task {data['data']['id']} not found for update")
    except Exception as e:
        print(f"❌ Kafka Consumer Error: {e}")
    finally:
        await consumer.stop()
        print("✅ Kafka Consumer Stopped.")

if __name__ == "__main__":
    try:
        asyncio.run(consume())
    except KeyboardInterrupt:
        print("❌ Consumer Stopped!")
