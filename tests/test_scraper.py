import pytest
from unittest.mock import AsyncMock, MagicMock
import sys
import os
from pathlib import Path
from telethon.tl.types import MessageMediaPhoto

# Add the project root directory to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.scraping import scrape_channel

@pytest.fixture
def mock_client():
    client = AsyncMock()
    # Create a proper async iterator for iter_messages
    async def async_iter(*args, **kwargs):
        return iter([])  # Default to empty iterator
    client.iter_messages = async_iter
    return client

@pytest.fixture
def mock_writer():
    return MagicMock()

@pytest.fixture
def mock_text_message():
    message = MagicMock()
    message.text = "Test message"
    message.id = 1
    message.date = "2024-01-01"
    message.media = None
    return message

@pytest.fixture
def mock_image_message():
    message = MagicMock()
    message.text = None
    message.id = 2
    message.date = "2024-01-01"
    
    # Create a mock photo object that looks like MessageMediaPhoto
    mock_photo = MagicMock(spec=MessageMediaPhoto)
    mock_photo.photo = True
    message.media = mock_photo
    return message

@pytest.mark.asyncio
async def test_scrape_text_message(mock_client, mock_writer, mock_text_message):
    """Test scraping a text-only message"""
    # Set up the async iterator to return our mock message
    async def mock_iter_messages(*args, **kwargs):
        yield mock_text_message
    mock_client.iter_messages = mock_iter_messages
    
    # Call the function
    await scrape_channel(mock_client, "@test_channel", mock_writer)
    
    # Verify the writer was called with correct data
    mock_writer.writerow.assert_called_once_with([
        "@test_channel",
        1,
        "Test message",
        "2024-01-01"
    ])

@pytest.mark.asyncio
async def test_scrape_image_message(mock_client, mock_writer, mock_image_message):
    """Test scraping a message with an image"""
    # Set up the async iterator
    async def mock_iter_messages(*args, **kwargs):
        yield mock_image_message
    mock_client.iter_messages = mock_iter_messages
    
    # Mock the download_media method
    mock_client.download_media = AsyncMock()
    mock_client.download_media.return_value = "test_image.jpg"
    
    # Call the function
    await scrape_channel(mock_client, "@test_channel", mock_writer)
    
    # Verify download_media was called
    mock_client.download_media.assert_called_once()

@pytest.mark.asyncio
async def test_scrape_multiple_messages(
    mock_client,
    mock_writer,
    mock_text_message,
    mock_image_message
):
    """Test scraping multiple messages"""
    # Set up the async iterator
    async def mock_iter_messages(*args, **kwargs):
        yield mock_text_message
        yield mock_image_message
    mock_client.iter_messages = mock_iter_messages
    
    # Mock the download_media method
    mock_client.download_media = AsyncMock()
    mock_client.download_media.return_value = "test_image.jpg"
    
    # Call the function
    await scrape_channel(mock_client, "@test_channel", mock_writer)
    
    # Verify writer was called for text message
    mock_writer.writerow.assert_called_once_with([
        "@test_channel",
        1,
        "Test message",
        "2024-01-01"
    ])
    
    # Verify download_media was called for image message
    mock_client.download_media.assert_called_once()

@pytest.mark.asyncio
async def test_max_messages_limit(mock_client, mock_writer, mock_text_message):
    """Test that scraping respects MAX_MESSAGES limit"""
    # Set up the async iterator to yield many messages
    async def mock_iter_messages(*args, **kwargs):
        for _ in range(15000):  # More than MAX_MESSAGES
            yield mock_text_message
    mock_client.iter_messages = mock_iter_messages
    
    # Call the function
    await scrape_channel(mock_client, "@test_channel", mock_writer)
    
    # Verify that only MAX_MESSAGES were processed
    assert mock_writer.writerow.call_count <= 10000

@pytest.mark.asyncio
async def test_error_handling(mock_client, mock_writer):
    """Test error handling during scraping"""
    # Configure mock client to raise an exception
    async def mock_iter_messages(*args, **kwargs):
        # Raise exception immediately without creating a coroutine
        raise Exception("Test error")
        # This line is never reached but prevents the warning
        yield None
    mock_client.iter_messages = mock_iter_messages
    
    # Call the function
    await scrape_channel(mock_client, "@test_channel", mock_writer)
    
    # Verify no data was written
    mock_writer.writerow.assert_not_called()

@pytest.mark.asyncio
async def test_empty_channel(mock_client, mock_writer):
    """Test handling of empty channel"""
    # Configure mock client to return no messages
    async def mock_iter_messages(*args, **kwargs):
        if False:  # This ensures the generator is empty
            yield
    mock_client.iter_messages = mock_iter_messages
    
    # Call the function
    await scrape_channel(mock_client, "@test_channel", mock_writer)
    
    # Verify no data was written
    mock_writer.writerow.assert_not_called()