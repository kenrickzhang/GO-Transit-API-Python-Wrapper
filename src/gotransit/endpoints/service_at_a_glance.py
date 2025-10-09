class ServiceAtAGlance:
    def __init__(self, client):
        self.client = client

    def buses_all(self, params: dict = None):
        return self.client._request("api/V1/ServiceataGlance/Buses/All", params)

    def trains_all(self, params: dict = None):
        return self.client._request("api/V1/ServiceataGlance/Trains/All", params)

    def upx_all(self, params: dict = None):
        return self.client._request("api/V1/ServiceataGlance/UPX/All", params)
