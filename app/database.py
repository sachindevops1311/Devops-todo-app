import psycopg2
import os

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", 5432),
        database=os.getenv("DB_NAME", "tododb"),
        user=os.getenv("DB_USER", "todouser"),
        password=os.getenv("DB_PASSWORD", "todopassword")
    )
    return conn
