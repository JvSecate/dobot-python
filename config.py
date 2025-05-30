import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the serial port from environment variable with a fallback to the original value
DOBOT_SERIAL_PORT = os.environ.get('DOBOT_SERIAL_PORT', '/dev/tty.SLAB_USBtoUART') 