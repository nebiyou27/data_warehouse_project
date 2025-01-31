import pytest
from unittest.mock import MagicMock, call
from telethon.tl.custom.message import Message
from scraping import scrape_channel

@pytest.mark.asyncio
async def test_scrape_channel():
    """Test scrape_channel function with mocked dependencies.
    
    Verifies that:
    1. Messages are properly iterated from the client
    2. Both messages are processed and written
    3. Proper error handling exists for media access
    """
    # Arrange - Setup test doubles
    mock_client = MagicMock()
    mock_writer = MagicMock()

    # Create realistic message mocks with required attributes
    def create_mock_message(msg_id, text, date):
        message = MagicMock(spec=Message)
        message.id = msg_id
        message.text = text
        message.date = date
        message.media = None  # Explicitly set missing attribute from error
        return message

    # Create test messages
    messages = [
        create_mock_message(1, "Test message 1", "2024-01-30"),
        create_mock_message(2, "Test message 2", "2024-01-31")
    ]

    # Configure client to return async message iterator
    async def mock_iter_messages(*args, **kwargs):
        for msg in messages:
            yield msg

    mock_client.iter_messages = mock_iter_messages

    # Act - Execute the function under test
    await scrape_channel(mock_client, "@test_channel", mock_writer)

    # Assert - Verify correct interactions
    # Check writer was called exactly twice
    assert mock_writer.writerow.call_count == 2, \
        "Should write exactly two messages"
        
    # Verify both messages were processed
    mock_writer.writerow.assert_has_calls([
        call([ "@test_channel", 1, "Test message 1", "2024-01-30"]),
        call([ "@test_channel", 2, "Test message 2", "2024-01-31"])
    ], any_order=False)
