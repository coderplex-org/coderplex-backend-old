# sample code to connect to database and list out the tables.
# To be removed once verified
# input valid credentials before testing.
import psycopg2
test = psycopg2.connect(
    database="coderplex",
    user="test",
    password="test123",
    host="127.0.0.1",
    port="5432")
cursor = test.cursor()
cursor.execute(
    "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
)
for table in cursor.fetchall():
    print(table)
