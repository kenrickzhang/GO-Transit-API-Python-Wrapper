from gotransit import Client, Stop

def main():
    client = Client()
    stop_api = Stop(client)

    stop_code = "1234"  # replace with a real stop code
    try:
        data = stop_api.next_service(stop_code)
        print(data)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
