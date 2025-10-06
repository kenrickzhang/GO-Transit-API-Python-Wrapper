from api import *
import json

def main():
    try:
        result = get_stop_nextservice("UN")

        with open("response.json", "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

        print("API response saved to response.json")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
