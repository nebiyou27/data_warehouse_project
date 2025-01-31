import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from dotenv import load_dotenv

def test_env_variables():
    """Test if environment variables are loaded correctly."""
    load_dotenv()
    assert os.getenv("API_ID") is not None, "API_ID is missing"
    assert os.getenv("API_HASH") is not None, "API_HASH is missing"
