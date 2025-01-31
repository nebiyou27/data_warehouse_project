import csv
import os
import logging
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from src.logging_config import setup_logging


# Load environment variables
load_dotenv()

# Get API credentials from the .env file
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')

# Output directories
TEXT_DATA_DIR = "data/raw/"
IMAGE_DATA_DIR = "data/images/"

# Ensure directories exist
os.makedirs(TEXT_DATA_DIR, exist_ok=True)
os.makedirs(IMAGE_DATA_DIR, exist_ok=True)

# CSV file path for text data
csv_file_path = os.path.join(TEXT_DATA_DIR, "telegram_data.csv")

# Maximum number of messages to scrape per channel
MAX_MESSAGES = 10000 

# Set up logging
logger = setup_logging()


async def scrape_channel(client, channel_name, writer):
    """
    Scrapes messages and images from a Telegram channel.

    Args:
        client: The Telegram client instance.
        channel_name: The Telegram channel to scrape.
        writer: The CSV writer to write the scraped data.
    """
    logger.info(f"Scraping {channel_name} started.")
    message_count = 0

    try:
        # Iterate through the messages in the channel
        async for message in client.iter_messages(channel_name):
            if message_count >= MAX_MESSAGES:
                break 

            # Save text messages
            if message.text:
                logger.debug(f"Scraping message {message.id}: {message.text[:50]}...") 
                writer.writerow([channel_name, message.id, message.text, message.date])

            # Save images if present
            if message.media and isinstance(message.media, MessageMediaPhoto):
                image_path = os.path.join(IMAGE_DATA_DIR, f"{channel_name}_{message.id}.jpg")
                await client.download_media(message.media, file=image_path)
                logger.info(f"Saved image: {image_path}")

            message_count += 1

    except Exception as e:
        logger.error(f"Error scraping {channel_name}: {e}")
        return

    logger.info(f"Scraping {channel_name} completed. {message_count} messages scraped.")


async def main():
    """
    Main function to scrape messages from a list of channels.
    """
    # Initialize the Telegram client
    async with TelegramClient('scraping_session', api_id, api_hash) as client:
        await client.start()

        # Open CSV file for writing text data
        try:
            with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Channel Name', 'Message ID', 'Message', 'Date'])

                # List of channels to scrape
                channels = [
                    "@DoctorsET",
                    "Chemed",
                    "@lobelia4cosmetics",
                    "@yetenaweg",
                    "@EAHCI",
                ]

                # Iterate over the channels and scrape data
                for channel in channels:
                    await scrape_channel(client, channel, writer)

        except Exception as e:
            logger.error(f"Error opening CSV file for writing: {e}")
            return

    logger.info(f"Text data saved in {csv_file_path}")
    logger.info(f"Images saved in {IMAGE_DATA_DIR}")


# Run the main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
