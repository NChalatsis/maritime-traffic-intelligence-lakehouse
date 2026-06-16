from pyspark.sql import functions as F
from pyspark.sql import types as T

num_events = 50000

df = (
    spark.range(num_events)
    .withColumn(
        "vessel_id",
        F.concat(F.lit("V"), F.lpad((F.rand() * 500).cast("int"), 4, "0"))
    )
    .withColumn(
        "event_timestamp",
        F.expr("timestamp('2025-01-01 00:00:00')") + F.expr("INTERVAL 1 MINUTE") * (F.rand() * 43200).cast("int")
    )
    .withColumn(
        "latitude",
        F.round(F.lit(37.5) + (F.rand() * 1.0), 6)
    )
    .withColumn(
        "longitude",
        F.round(F.lit(23.0) + (F.rand() * 1.5), 6)
    )
    .withColumn(
        "speed_knots",
        F.round(F.rand() * 25, 2)
    )
    .withColumn(
        "heading",
        F.round(F.rand() * 360, 2)
    )
    .drop("id")
)

display(df.limit(20))

#save as delta table
df.write.format("delta").mode("overwrite").saveAsTable("bronze_ais_events")