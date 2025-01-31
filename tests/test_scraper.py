import pytest
from unittest.mock import AsyncMock, MagicMock
from telethon.tl.custom.message import Message
from src.scraping import scrape_channel

@pytest.mark.asyncio
async def test_scrape_channel():
    """Test scrape_channel function by mocking TelegramClient and messages."""

    # Mock Telegram client and writer
    mock_client = AsyncMock()
    mock_writer = MagicMock()

    # Mock messages
    mock_message_1 = MagicMock(spec=Message)
    mock_message_1.id = 1
    mock_message_1.text = "Test message 1"
    mock_message_1.date = "2024-01-30"

    mock_message_2 = MagicMock(spec=Message)
    mock_message_2.id = 2
    mock_message_2.text = "Test message 2"
    mock_message_2.date = "2024-01-31"

    # Mock the client to return these messages
    mock_client.iter_messages.return_value = [mock_message_1, mock_message_2]

    # Call the function with mock client and writer
    await scrape_channel(mock_client, "@test_channel", mock_writer)

    # Ensure messages were written
    mock_writer.write.assert_called()
