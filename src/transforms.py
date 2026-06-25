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
