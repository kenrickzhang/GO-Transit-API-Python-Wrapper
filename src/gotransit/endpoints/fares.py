class Fares:
    def __init__(self, client):
        self.client = client

    def get(self, from_stop: str, to_stop: str, operational_day: str = None, params: dict = None):
        if operational_day:
            endpoint = f"api/V1/Fares/{from_stop}/{to_stop}/{operational_day}"
        else:
            endpoint = f"api/V1/Fares/{from_stop}/{to_stop}"
        return self.client._request(endpoint, params)
