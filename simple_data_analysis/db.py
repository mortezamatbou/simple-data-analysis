import mysql.connector
import os

# print(os.environ.get('DB_DATABASE'))
# exit()

try:
    conn = mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USERNAME'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_DATABASE'),
        port=os.environ.get('DB_MACHINE_PORT')
    )
    db = conn.cursor(dictionary=True, buffered=True)
except Exception as e:
    print(e)
    exit()
