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
cleaned_data_path = r"C:\Users\neba\Desktop\data_warehouse_project\data\cleaned\cleaned_telegram_data.csv"

# Configure logging
log_file = os.path.join(os.path.dirname(cleaned_data_path), "store_cleaned_data.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

print("🚀 Storing Cleaned Data to Database...")
logging.info("🚀 Database Storage Process Started!")

# Load cleaned data
try:
    df = pd.read_csv(cleaned_data_path)
    print(f"✅ CSV file '{cleaned_data_path}' loaded successfully.")
    logging.info(f"✅ CSV file '{cleaned_data_path}' loaded successfully.")
except Exception as e:
    logging.error(f"❌ Error loading CSV file: {e}")
    raise

# Establish database connection
try:
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )
    cursor = conn.cursor()
    print("✅ Database connection established.")
    logging.info("✅ Database connection established.")
except Exception as e:
    logging.error(f"❌ Database connection error: {e}")
    raise

# Create table if not exists
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

# Insert cleaned data
insert_query = """
INSERT INTO telegram_messages (channel_name, message_id, text, date, emoji_used)
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

# Close database connection
cursor.close()
conn.close()
print("🚀 Database Storage Process Completed!")
logging.info("🚀 Database Storage Process Completed!")
