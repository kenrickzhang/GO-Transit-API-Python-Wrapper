import json
from gotransit import Client, Stop

def main():
    client = Client()
    stop_api = Stop(client)

    stop_code = "UN"
    try:
        data = stop_api.next_service(stop_code)
        
        with open("response.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        
        print("API Response ==> response.json")
        
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
