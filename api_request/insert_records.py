from weather_api import mock_fetch_data, fetch_data
import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host="database",
            user="allan",
            port=5432,
            password="123456789",
            dbname="weather_data"
        )
        print("Connected to database!")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        raise

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
           CREATE SCHEMA IF NOT EXISTS dev;
           CREATE TABLE IF NOT EXISTS dev.weather_data(
            id SERIAL PRIMARY KEY,
            city TEXT,
            temperature FLOAT,
            weather_descriptions TEXT,
            wind_speed FLOAT,
            time TIMESTAMP,
            inserted_at TIMESTAMP DEFAULT NOW(),
            utc_offset FLOAT
           );
        """)
        conn.commit()
        print("table was created successfully!!!")
    except psycopg2.Error as error:
        print(f" Error creating table: {error}")
        raise 
def insert_records(conn, data):
    try:
        print("Insterting weather data into database")
        weather = data['current']
        location = data['location']
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.weather_data(
                city,
                temperature,
                weather_descriptions,
                wind_speed,
                time,
                inserted_at,
                utc_offset
                ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        """,(
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        ))
        conn.commit()
        print(" Records inserted successfully!!!")
    except psycopg2.Error as error:
        print(f" Error inserting records: {error}")
        raise
            
def main():
    try:
        #data=mock_fetch_data()
        data=fetch_data()
        print(data)
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
        print("All operations completed successfully!!!")
    except Exception as e:
        print(f"Error: {e}")
        raise
    finally:
        if 'conn' in locals():
            conn.close()
            print("Connection closed")
    