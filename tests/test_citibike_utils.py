import os
import sys

sys.path.append(os.getcwd())

import datetime
from src.citibike.citibike_utils import get_trip_duration_mins

def test_get_trip_duration_mins(spark):
    
    # Create a sample DataFrame
    data = [
        (datetime.datetime(2025, 4, 10, 10, 0, 0), datetime.datetime(2025, 4, 10, 10, 10, 0)),
        (datetime.datetime(2025, 4, 10, 10, 0, 0), datetime.datetime(2025, 4, 10, 10, 30, 0)),
    ]

    df = spark.createDataFrame(data, "start_time timestamp, end_time timestamp")

    # Apply the function
    result_df = get_trip_duration_mins(spark, df, 'start_time', 'end_time', 'trip_duration_mins')

    results = result_df.select('trip_duration_mins').collect()

    assert results[0]['trip_duration_mins'] == 10
    assert results[1]['trip_duration_mins'] == 30