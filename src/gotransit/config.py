from pathlib import Path
from dotenv import load_dotenv
import os

current = Path(__file__).resolve()
for _ in range(5):  # check up to 5 parent directories
    env_path = current / ".env"
    if env_path.exists():
        load_dotenv(env_path)
        break
    current = current.parent

GO_TRANSIT_API_KEY = os.getenv("GO_TRANSIT_API_KEY")
if not GO_TRANSIT_API_KEY:
    raise ValueError(
        "Error: GO Transit API key not found. Please set GO_TRANSIT_API_KEY in your environment or .env file."
    )
