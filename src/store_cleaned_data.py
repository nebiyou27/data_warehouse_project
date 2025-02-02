import pandas as pd
import psycopg2
import os
import logging

# Database connection parameters
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "telegram_data"
DB_USER = "postgres"
DB_PASSWORD = "neba"

# Define file paths
CLEANED_DATA_PATH = (
    r"C:\Users\neba\Desktop\data_warehouse_project\data\cleaned"
    r"\cleaned_telegram_data.csv"
)

# Configure logging
LOG_FILE = os.path.join(
    os.path.dirname(CLEANED_DATA_PATH), "store_cleaned_data.log"
)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

print("🚀 Storing Cleaned Data to Database...")
logging.info("🚀 Database Storage Process Started!")


def load_csv(file_path):
    """Load cleaned CSV file into a Pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        print(f"✅ CSV file '{file_path}' loaded successfully.")
        logging.info(f"✅ CSV file '{file_path}' loaded successfully.")
        return df
    except Exception as e:
        logging.error(f"❌ Error loading CSV file: {e}")
        raise


def connect_to_db():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST, port=DB_PORT, database=DB_NAME,
            user=DB_USER, password=DB_PASSWORD
        )
        cursor = conn.cursor()
        print("✅ Database connection established.")
        logging.info("✅ Database connection established.")
        return conn, cursor
    except Exception as e:
        logging.error(f"❌ Database connection error: {e}")
        raise


def create_table(cursor, conn):
    """Create the 'telegram_messages' table if it does not exist."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS telegram_messages (
        channel_name TEXT,
        message_id BIGINT PRIMARY KEY,
        text TEXT,
        date TIMESTAMP,
        emoji_used TEXT
    );
    """
    try:
        cursor.execute(create_table_query)
        conn.commit()
        print("✅ Table 'telegram_messages' ensured.")
        logging.info("✅ Table 'telegram_messages' ensured.")
    except Exception as e:
        logging.error(f"❌ Error creating table: {e}")
        raise


def insert_cleaned_data(df, cursor, conn):
    """Insert cleaned data into the database, avoiding duplicate entries."""
    insert_query = """
        INSERT INTO telegram_messages (channel_name, message_id, text, date,
                                   emoji_used)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (message_id) DO NOTHING;
    """
    try:
        for _, row in df.iterrows():
            cursor.execute(insert_query, tuple(row))
        conn.commit()
        print("✅ Cleaned data stored successfully.")
        logging.info("✅ Cleaned data stored successfully.")
    except Exception as e:
        logging.error(f"❌ Error inserting data: {e}")
        raise


def main():
    """Main function to execute the storage process."""
    df = load_csv(CLEANED_DATA_PATH)
    conn, cursor = connect_to_db()
    create_table(cursor, conn)
    insert_cleaned_data(df, cursor, conn)

    # Close database connection
    cursor.close()
    conn.close()
    print("🚀 Database Storage Process Completed!")
    logging.info("🚀 Database Storage Process Completed!")


if __name__ == "__main__":
    main()
