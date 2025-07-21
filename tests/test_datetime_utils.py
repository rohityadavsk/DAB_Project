import os
import sys

sys.path.append(os.getcwd())

import datetime
from src.utils.datetime_utils import timestamp_to_date_col

def test_timestamp_to_date_col(spark):
    
    # Create a sample DataFrame
    data = [
        (datetime.datetime(2025, 4, 11, 12, 30, 0),),
    ]

    df = spark.createDataFrame(data, "ride_timestamp timestamp")

    # Apply the function
    result_df = timestamp_to_date_col(spark, df, 'ride_timestamp', 'ride_date')

    row = result_df.select('ride_date').first()

    expected_date = datetime.date(2025, 4, 11)

    assert row['ride_date'] == expected_date