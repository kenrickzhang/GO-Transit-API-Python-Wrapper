class Stop:
    def __init__(self, client):
        self.client = client

    def next_service(self, stop_code: str, params: dict = None):
        return self.client._request(f"api/V1/Stop/NextService/{stop_code}", params)

    def details(self, stop_code: str, params: dict = None):
        return self.client._request(f"api/V1/Stop/Details/{stop_code}", params)

    def destinations(self, stop_code: str, from_time: str, to_time: str, params: dict = None):
        return self.client._request(f"api/V1/Stop/Destinations/{stop_code}/{from_time}/{to_time}", params)

    def all(self, params: dict = None):
        return self.client._request("api/V1/Stop/All", params)
