class UPGTFS:
    def __init__(self, client):
        self.client = client

    def alerts(self, params: dict = None):
        return self.client._request("api/V1/UP/Gtfs/Feed/Alerts", params)

    def trip_updates(self, params: dict = None):
        return self.client._request("api/V1/UP/Gtfs/Feed/TripUpdates", params)

    def vehicle_positions(self, params: dict = None):
        return self.client._request("api/V1/UP/Gtfs/Feed/VehiclePosition", params)
