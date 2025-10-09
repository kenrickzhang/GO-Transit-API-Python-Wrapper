class ServiceUpdate:
    def __init__(self, client):
        self.client = client

    def service_alerts_all(self, params: dict = None):
        return self.client._request("api/V1/ServiceUpdate/ServiceAlert/All", params)

    def info_alerts_all(self, params: dict = None):
        return self.client._request("api/V1/ServiceUpdate/InformationAlert/All", params)

    def marketing_alerts_all(self, params: dict = None):
        return self.client._request("api/V1/ServiceUpdate/MarketingAlert/All", params)

    def union_departures_all(self, params: dict = None):
        return self.client._request("api/V1/ServiceUpdate/UnionDepartures/All", params)

    def service_guarantee(self, trip_number: str, operational_day: str, params: dict = None):
        return self.client._request(f"api/V1/ServiceUpdate/ServiceGuarantee/{trip_number}/{operational_day}", params)

    def exceptions_train(self, params: dict = None):
        return self.client._request("api/V1/ServiceUpdate/Exceptions/Train", params)

    def exceptions_bus(self, params: dict = None):
        return self.client._request("api/V1/ServiceUpdate/Exceptions/Bus", params)

    def exceptions_all(self, params: dict = None):
        return self.client._request("api/V1/ServiceUpdate/Exceptions/All", params)
