# What is it?

Module `forecast` designated to make predictions irradiance from photovoltaic
modules based on meteorological features.

This can be used on two types of prediction:
* Mapped Station
* New point from the map

In any of these scenarios, will be received a `json` file containing the list of 
hours to be predicted for a Station.

# How it works?

The forecast service will receive a list of `Feature` object containing the 
values from meteorological features for each hour and station in predict range. 
The processed `Feature` object will look like:

```python
import numpy as np

from domain.data import Features
from domain.station import Station
from domain.coordinates import Coordinates

job = [
    Features(
        data=np.array([0, 1, 2, 3, 4, 5]),
        name="feature_name",
        hour="hour_x",
        station=Station(
            name="station_name", 
            coordinates=Coordinates(latitude=90, longitude=90)
        ),
        features_names=["feat1", "feat2", ...]
    )
]
```

# How request the forecast?

The table below show the fields from request a forecast.

> [!IMPORTANT]  
> Use field `station` to forecast mapped stations and field `coordinates` to 
> forecast new points in the map. DO NOT use both of them in the same request.


| **Field**           	           | **Type** 	  | **Necessary?** 	 | **Description**                                              	                                               |
|---------------------------------|:-----------:|:----------------:|--------------------------------------------------------------------------------------------------------------|
| _station_                     	 |  str    	   |   Yes       	    | Station Name. If it's a new station, this can be a optional field.                                        	  |
| _coordinates_                 	 |  map    	   |  Optional    	   | Coordinates with Latitude and Longitude for the station. Required if it's a new station.                  	  |
| _coordinates.latitude_        	 |  float   	  |  Optional    	   | Latitude corresponds to interval [-90, +90]                                                               	  |
| _coordinates.longitude_       	 |  float   	  |  Optional    	   | Longitude corresponds to interval [-90, +90]                                                              	  |
| _data_                        	 | list[map] 	 |   Yes       	    | Data used to extract the features to realize the inference.                                               	  |
| _data.hour_                   	 |  int    	   |   Yes       	    | Hour of prediction                                                                                        	  |
| _data.temperature_C_          	 |  float   	  |   Yes       	    | Air Temperature in Celsius                                                                                	  |
| _data.wind_speed_ms_          	 |  float   	  |   Yes       	    | Wind Speed in meters per second (m/s)                                                                     	  |
| _data.wind_direction_         	 |  str    	   |   Yes       	    | Wind Direction corresponds to a direction in the map (Available: "N", "S", "E", "W" and its combinations) 	  |
| _data.pressure_atm_           	 |  float   	  |   Yes       	    | Air pressure in Atmosphere (ATM)                                                                           	 |
| _data.altitude_m_             	 |  float   	  |   Yes       	    | Altitude in meters (m)                                                                                    	  |
| _data.humidity_percentual_    	 |  float   	  |   Yes       	    | Percentual of Air Humidity (between 0 and 1)                                                              	  |
| _data.rain_mm_                	 |  float   	  |   Yes       	    | Rain measured in millimeters per hour (mm/h)                                                               	 |
| _data.cloud_cover_percentual_ 	 |  float   	  |   Yes       	    | Percentual for cloud cover (between 0 and 1)                                                              	  |


<details>

<summary>Sample request for Forecast Service</summary>

```json
{
  "station": "station_name",
  "coordinates": {
    "latitude": 90,
    "longitude": 10
  },
  "data":[
    {
      "hour": 1,
      "temperature_C": 10,
      "wind_speed_ms": 1,
      "wind_direction": "s",
      "pressure_atm": 1000,
      "altitude_m": 1010,
      "humidity_percentual": 0.6,
      "rain_mm": 0,
      "cloud_cover_percentual": 0.1
    },
    {
      "hour": 2,
      "temperature_C": 10,
      "wind_speed_ms": 1,
      "wind_direction": "s",
      "pressure_atm": 1000,
      "altitude_m": 1010,
      "humidity_percentual": 0.6,
      "rain_mm": 0,
      "cloud_cover_percentual": 0.1
    },
    {
      "hour": 10,
      "temperature_C": 10,
      "wind_speed_ms": 1,
      "wind_direction": "s",
      "pressure_atm": 1000,
      "altitude_m": 1010,
      "humidity_percentual": 0.6,
      "rain_mm": 0,
      "cloud_cover_percentual": 0.1
    }
  ]
}
```

</details>

