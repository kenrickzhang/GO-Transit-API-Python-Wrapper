import requests
from config import GO_TRANSIT_API_KEY

BASE_URL = "https://api.openmetrolinx.com/OpenDataAPI"

def get_data_api(endpoint: str, params: dict = None):

    headers = {
        "User-Agent": "GTPY/1.0",
        "Accept": "application/json",
        }
    
    if params is None:
        params = {}
    
    params["key"] = GO_TRANSIT_API_KEY  
    
    url = f"{BASE_URL}/{endpoint}"

    # print(f"Called GET {url}")
    response = requests.get(url, headers=headers, params=params)

    if response.ok:
        return response.json()
    else:
        raise RuntimeError(
            f"API GET failed: {response.status_code} - {response.text}"
        )


# UPGTFSRealTimeV1

def get_up_gtfs_feed_alerts(params: dict = None):
    return get_data_api(endpoint=f"api/V1/UP/Gtfs/Feed/Alerts", params=params)

def get_up_gtfs_feed_tripupdates(params: dict = None):
    return get_data_api(endpoint=f"api/V1/UP/Gtfs/Feed/TripUpdates", params=params)

def get_up_gtfs_feed_vehicleposition(params: dict = None):
    return get_data_api(endpoint=f"api/V1/UP/Gtfs/Feed/VehiclePosition", params=params)


# Stop

def get_stop_nextservice(stop_code: str, params: dict = None):
    return get_data_api(endpoint=f"api/V1/Stop/NextService/{stop_code}", params=params)

def get_stop_details(stop_code: str, params: dict = None):
    return get_data_api(endpoint=f"api/V1/Stop/Details/{stop_code}", params=params)

def get_stop_destinations(stop_code: str, from_time: str, to_time: str,  params: dict = None):
    return get_data_api(endpoint=f"api/V1/Stop/Destinations/{stop_code}/{from_time}/{to_time}", params=params)

def get_stop_all(params: dict = None):
    return get_data_api(endpoint=f"api/V1/Stop/All", params=params)


# Service Update

def get_serviceupdate_servicealert_all(params: dict = None):
    return get_data_api(endpoint="api/V1/ServiceUpdate/ServiceAlert/All", params=params)

def get_serviceupdate_information_all(params: dict = None):
    return get_data_api(endpoint="api/V1/ServiceUpdate/InformationAlert/All", params=params)

def get_serviceupdate_marketingalert_all(params: dict = None):
    return get_data_api(endpoint="api/V1/ServiceUpdate/MarketingAlert/All", params=params)

def get_serviceupdate_uniondepartures_all(params: dict = None):
    return get_data_api(endpoint="api/V1/ServiceUpdate/UnionDepartures/All", params=params)

def get_serviceupdate_serviceguarantee(trip_number: str, operational_day: str, params: dict = None):
    return get_data_api(endpoint=f"api/V1/ServiceUpdate/ServiceGuarantee/{trip_number}/{operational_day}", params=params)

def get_serviceupdate_exceptions_train(params: dict = None):
    return get_data_api(endpoint="api/V1/ServiceUpdate/Exceptions/Train", params=params)

def get_serviceupdate_exceptions_bus(params: dict = None):
    return get_data_api(endpoint="api/V1/ServiceUpdate/Exceptions/Bus", params=params)

def get_serviceupdate_exceptions_all(params: dict = None):
    return get_data_api(endpoint="api/V1/ServiceUpdate/Exceptions/All", params=params)


# Service At Glance

def get_servicataglance_buses_all(params: dict = None):
    return get_data_api(endpoint="api/V1/ServiceataGlance/Buses/All", params=params)

def get_servicataglance_trains_all(params: dict = None):
    return get_data_api(endpoint="api/V1/ServiceataGlance/Trains/All", params=params)

def get_servicataglance_upx_all(params: dict = None):
    return get_data_api(endpoint="api/V1/ServiceataGlance/UPX/All", params=params)


# Schedule

def get_schedule_journey(date: str, from_stop_code: str, to_stop_code: str, start_time: str, max_journey: str, params: dict = None):
    return get_data_api(endpoint=f"api/V1/Schedule/Journey/{date}/{from_stop_code}/{to_stop_code}/{start_time}/{max_journey}", params=params)

def get_schedule_line(date: str, line_code: str, line_direction: str, params: dict = None):
    return get_data_api(endpoint=f"api/V1/Schedule/Line/{date}/{line_code}/{line_direction}", params=params)

def get_schedule_line_all(date: str, params: dict = None):
    return get_data_api(endpoint=f"api/V1/Schedule/Line/All/{date}", params=params)

def get_schedule_line_stop(date: str, line_code: str, line_direction: str, params: dict = None):
    return get_data_api(endpoint=f"api/V1/Schedule/Line/Stop/{date}/{line_code}/{line_direction}", params=params)

def get_schedule_trip(date: str, trip_number: str, params: dict = None):
    return get_data_api(endpoint=f"api/V1/Schedule/Trip/{date}/{trip_number}", params=params)


# GTFS Feeds

def get_gtfs_feed_alerts(params: dict = None):
    return get_data_api(endpoint="api/V1/Gtfs/Feed/Alerts", params=params)

def get_gtfs_feed_tripupdates(params: dict = None):
    return get_data_api(endpoint="api/V1/Gtfs/Feed/TripUpdates", params=params)

def get_gtfs_feed_vehicleposition(params: dict = None):
    return get_data_api(endpoint="api/V1/Gtfs/Feed/VehiclePosition", params=params)


# Fleet (deprecated)


# Fare

def get_fares(from_stop_code: str, to_stop_code: str, operational_day: str = None, params: dict = None):
    if operational_day is None:
        return get_data_api(endpoint=f"api/V1/Fares/{from_stop_code}/{to_stop_code}", params=params)
    else:
        return get_data_api(endpoint=f"api/V1/Fares/{from_stop_code}/{to_stop_code}/{operational_day}", params=params)