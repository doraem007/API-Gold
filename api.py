from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
import mysql.connector
import os

app = FastAPI(docs_url="/documentation", redoc_url=None)

# เชื่อมต่อกับฐานข้อมูล MySQL
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        port=os.getenv('MYSQL_PORT'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )

# Ensure the table exists
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id VARCHAR(255) PRIMARY KEY)''')
conn.commit()
conn.close()

class EventSource(BaseModel):
    userId: str
    type: str

class Event(BaseModel):
    type: str
    replyToken: str
    source: EventSource
    timestamp: int

class WebhookRequest(BaseModel):
    events: List[Event]

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    webhook_request = WebhookRequest(**data)
    
    conn = get_db_connection()
    cursor = conn.cursor()

    for event in webhook_request.events:
        if event.type == "follow":
            user_id = event.source.userId
            try:
                cursor.execute('INSERT IGNORE INTO users (user_id) VALUES (%s)', (user_id,))
                conn.commit()
                print(f"New follower: {user_id}")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                conn.rollback()
    
    cursor.close()
    conn.close()

    return {"status": "success"}
