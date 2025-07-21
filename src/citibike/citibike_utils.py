from pyspark.sql.functions import unix_timestamp, col 

def get_trip_duration_mins(spark, df, start_col, end_col, output_col):
    """
    Adds a column to the DataFrame calculate a difference in minutes between two timestamp columns.

    :param spark: Spark session
    :param df: Input DataFrame
    :param start_col: Name of the start timestamp column
    :param end_col: Name of the end timestamp column
    :param output_col: Name of the output column for the difference in minutes

    Returns:
        DataFrame with the new date column
    """
    return df.withColumn(output_col, (unix_timestamp(col(end_col)) - unix_timestamp(col(start_col))) / 60)