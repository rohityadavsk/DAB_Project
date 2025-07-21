from pyspark.sql.functions import to_date, col

def timestamp_to_date_col(spark, df, timestamp_col, output_col):
    """
    Extracts date from a timestamp column and adds it as a new column.

    :param spark: Spark session
    :param df: Input DataFrame
    :param timestamp_col: Name of the timestamp column
    :param output_col: Name of the output column for the ride date

    Returns:
        DataFrame with the new date column
    """
    return df.withColumn(output_col, to_date(col(timestamp_col)))