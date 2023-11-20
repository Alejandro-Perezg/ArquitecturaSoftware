import psycopg2
import csv

def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_schema.items (
            sku VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            description VARCHAR(255) NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            quantity INT NOT NULL,
            expdate DATE NOT NULL
        )
    """)

def insert_data(cursor, row):
    query = """
        INSERT INTO my_schema.items (sku, name, description, price, quantity, expiration_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (row["sku"], row["name"], row["description"], row["price"], row["quantity"], row["expdate"]))

def main():
    connection = psycopg2.connect("host=localhost dbname=my_database user=my_user password=my_password")

    with connection, connection.cursor() as cursor:
        create_table(cursor)

        with open('/home/jvnko/ArquitecturaSoftware/Proyecto-Final/model/sample_grocery.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                insert_data(cursor, row)

    print("data loaded....")

if __name__ == "__main__":
    main()
