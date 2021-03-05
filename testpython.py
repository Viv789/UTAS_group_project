conn = psycopg2.connect(
    host="localhost", database="cafe_data", user="postgres", password="docker"
)

mycursor = conn.cursor()