import sys
import os
import pytest

sys.path.append(os.getcwd())

@pytest.fixture()
def spark():
    # Create a Spark session
    try:
        from databricks.connect import DatabricksSession
        spark = DatabricksSession.builder.getOrCreate()
    except ImportError:
        try:
            # Fallback to local Spark session if databricks.connect is not available
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.getOrCreate()
        except:
            raise ImportError('Neither databricks.connect nor pyspark is available. Please install one of them to run the tests.')
    return spark