import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

def load_config(key):
    """Loads a configuration value from environment variables."""
    return os.environ.get(key)
