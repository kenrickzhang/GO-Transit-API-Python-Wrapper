import os
from dotenv import load_dotenv

load_dotenv()

GO_TRANSIT_API_KEY = os.getenv("GO_TRANSIT_API_KEY")

if not GO_TRANSIT_API_KEY:
    raise ValueError("Error: GO Transit API key not found.")