from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def validate_coordinates(df: DataFrame) -> DataFrame:
    """
    Keep only records with valid geographic coordinates.
    """

    return df.filter(
        F.col("latitude").between(-90, 90)
        &
        F.col("longitude").between(-180, 180)
    )

def add_silver_features(df: DataFrame) -> DataFrame:
    """
    Apply Silver layer transformations and derive business columns.
    """

    return (
        df
        .dropDuplicates(
            ["vessel_id", "event_timestamp", "latitude", "longitude"]
        )
        .withColumn(
            "event_date",
            F.to_date("event_timestamp")
        )
        .withColumn(
            "event_hour",
            F.hour("event_timestamp")
        )
        .withColumn(
            "speed_category",
            F.when(F.col("speed_knots") == 0, "stationary")
             .when(F.col("speed_knots") < 5, "slow")
             .when(F.col("speed_knots") < 15, "medium")
             .otherwise("fast")
        )
        .withColumn(
            "is_moving",
            F.col("speed_knots") > 0
        )
    )