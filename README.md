# GoTransit Python Wrapper

A Python wrapper for the [GO Transit / Metrolinx Open Data API](https://api.openmetrolinx.com/OpenDataAPI), allowing easy access to real-time transit data.

---

## Features

- Access next service times for stops
- Retrieve stop details and destinations
- Query train and bus schedules
- Fetch General Transit Feed Specification (GTFS) feeds: alerts, trip updates, vehicle positions
- Service updates: alerts, marketing, exceptions
- Fare lookup between stops
- Modular design: `Client` handles requests, while endpoint classes (e.g., `Stop`, `Schedule`) organize resources

---

## Installation

Requires **Python 3.7+**.

```bash
# Install editable version from local repository
git clone https://github.com/kenrickzhang/gotransitwrapper.git
cd gotransitwrapper
pip install -e .
```
