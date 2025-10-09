class Schedule:
    def __init__(self, client):
        self.client = client

    def journey(self, date: str, from_stop: str, to_stop: str, start_time: str, max_journey: str, params: dict = None):
        return self.client._request(
            f"api/V1/Schedule/Journey/{date}/{from_stop}/{to_stop}/{start_time}/{max_journey}",
            params
        )

    def line(self, date: str, line_code: str, line_direction: str, params: dict = None):
        return self.client._request(f"api/V1/Schedule/Line/{date}/{line_code}/{line_direction}", params)

    def line_all(self, date: str, params: dict = None):
        return self.client._request(f"api/V1/Schedule/Line/All/{date}", params)

    def line_stop(self, date: str, line_code: str, line_direction: str, params: dict = None):
        return self.client._request(f"api/V1/Schedule/Line/Stop/{date}/{line_code}/{line_direction}", params)

    def trip(self, date: str, trip_number: str, params: dict = None):
        return self.client._request(f"api/V1/Schedule/Trip/{date}/{trip_number}", params)
