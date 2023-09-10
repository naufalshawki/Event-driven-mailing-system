import os
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
sender_host = os.getenv("SENDER_HOST")
sender_port = os.getenv("SENDER_PORT")
kafka_topics = os.getenv("KAFKA_TOPICS")
kafka_server = os.getenv("KAFKA_SERVER")
kafka_username = os.getenv("KAFKA_USERNAME")
kafka_password = os.getenv("KAFKA_PASSWORD")
kafka_group = os.getenv("KAFKA_GROUP")
kafka_client = os.getenv("KAFKA_CLIENT")