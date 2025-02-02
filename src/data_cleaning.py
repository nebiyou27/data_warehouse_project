import pandas as pd
import re
import os
import logging

# Define file paths
RAW_DATA_PATH = (
    r"C:\Users\neba\Desktop\data_warehouse_project\data\raw"
    r"\telegram_data.csv"
)
CLEANED_DATA_PATH = (
    r"C:\Users\neba\Desktop\data_warehouse_project\data\cleaned"
    r"\cleaned_telegram_data.csv"
)

# Configure logging
LOG_FILE = os.path.join(
    os.path.dirname(CLEANED_DATA_PATH), "data_cleaning.log"
)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

print("🚀 Data Cleaning Process Started...")
logging.info("🚀 Data Cleaning Process Started!")


def remove_emojis(text):
    """Remove emojis from text."""
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U0001F300-\U0001F5FF"  # Symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # Transport & map symbols
        u"\U0001F700-\U0001F77F"  # Alchemical symbols
        u"\U0001F780-\U0001F7FF"  # Geometric shapes
        u"\U0001F800-\U0001F8FF"  # Supplemental symbols
        u"\U0001F900-\U0001F9FF"  # Supplemental symbols and pictographs
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", text)


def clean_data(df):
    """Apply cleaning operations to the DataFrame."""
    df["text"] = df["text"].astype(str).apply(remove_emojis)
    df["text"] = df["text"].str.strip().replace("", None)
    df = df.dropna(subset=["text"])
    return df


def main():
    """Main function to execute data cleaning."""
    try:
        df = pd.read_csv(RAW_DATA_PATH)
        print(f"✅ CSV file '{RAW_DATA_PATH}' loaded successfully.")
        logging.info(f"✅ CSV file '{RAW_DATA_PATH}' loaded successfully.")
    except Exception as e:
        logging.error(f"❌ Error loading CSV file: {e}")
        raise

    df = clean_data(df)

    df.to_csv(CLEANED_DATA_PATH, index=False)
    print(f"✅ Cleaned data saved to '{CLEANED_DATA_PATH}'.")
    logging.info(f"✅ Cleaned data saved to '{CLEANED_DATA_PATH}'.")


if __name__ == "__main__":
    main()
