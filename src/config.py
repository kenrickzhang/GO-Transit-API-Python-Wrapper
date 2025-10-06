import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

GO_TRANSIT_API_KEY = os.getenv("GO_TRANSIT_API_KEY")

if not GO_TRANSIT_API_KEY:
    raise ValueError(
        "Error: GO Transit API key not found. "
        "Please set GO_TRANSIT_API_KEY in your environment or .env file."
    )
