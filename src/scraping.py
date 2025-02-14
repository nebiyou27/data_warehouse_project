import csv
import os
import logging
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto

# Load environment variables
load_dotenv()

# Get API credentials from .env
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')

# Output directories
TEXT_DATA_DIR = "data/raw/"
IMAGE_DATA_DIR = "data/images/"
LOGS_DIR = "logs/"

# Ensure directories exist
os.makedirs(TEXT_DATA_DIR, exist_ok=True)
os.makedirs(IMAGE_DATA_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(LOGS_DIR, "scraping.log")),
        logging.FileHandler(os.path.join(LOGS_DIR, "error.log")),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# CSV file path
csv_file_path = os.path.join(TEXT_DATA_DIR, "telegram_data.csv")


async def scrape_channel(client, channel_name, writer, max_messages):
    msg = (
        f"Starting to scrape {channel_name} "
        f"(Max {max_messages} messages)..."
    )
    logger.info(msg)

    try:
        async for message in client.iter_messages(
                channel_name, limit=max_messages):
            # Save text messages
            if message.text:
                row = [channel_name, message.id, message.text, message.date]
                writer.writerow(row)

            # Save images separately
            if message.media and isinstance(message.media, MessageMediaPhoto):
                image_filename = f"{channel_name}_{message.id}.jpg"
                image_path = os.path.join(IMAGE_DATA_DIR, image_filename)
                await client.download_media(message.media, file=image_path)
                logger.info(f"Saved image: {image_path}")

        logger.info(f"Scraping completed for {channel_name}")

    except Exception as e:
        error_msg = f"Error scraping {channel_name}: {str(e)}"
        logger.error(error_msg, exc_info=True)


async def main():
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        headers = ['Channel Name', 'Message ID', 'Message', 'Date']
        writer.writerow(headers)

        channels = [
            "@Chemed",
            "@lobelia4cosmetics",
            "@yetenaweg",
            "@EAHCI",
            "@DoctorsET",
        ]

        for channel in channels:
            await scrape_channel(client, channel, writer, max_messages=500)

    logger.info("Scraping task completed successfully!")


if __name__ == "__main__":
    with TelegramClient('scraping_session', api_id, api_hash) as client:
        client.loop.run_until_complete(main())
