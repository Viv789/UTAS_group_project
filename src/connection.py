import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


HOST = os.environ.get("DB_HOST")
USER = os.environ.get("DB_USER")
PASSWORD = os.environ.get("DB_PASS")
DB = os.environ.get("DB_NAME")
PORT = int(os.environ.get("DB_PORT"))

# HOST = os.environ.get("LOCAL_DB_HOST")
# USER = os.environ.get("LOCAL_DB_USER")
# PASSWORD = os.environ.get("LOCAL_DB_PASS")
# DB = os.environ.get("LOCAL_DB_NAME")
# PORT = os.environ.get("LOCAL_DB_PORT")


def connection():
    return psycopg2.connect(
    host=HOST, database=DB, user=USER, password=PASSWORD, port=PORT)
