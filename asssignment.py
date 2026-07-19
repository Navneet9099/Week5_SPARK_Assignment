from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
from pyspark.sql.functions import col
from pyspark.sql.types import TimestampType
from pyspark.sql.functions import min, max, mean
# Create Spark Session
spark = SparkSession.builder \
    .appName("Week5 Spark Assignment") \
    .getOrCreate()

# Read CSV
df = spark.read.csv(
    "sales.csv",
    header=True,
    inferSchema=True
)
# ==========================
# Q15 - Final Data Processing Pipeline
# ==========================

from pyspark.sql.functions import sum

print("\n===== Q15: Final Data Processing Pipeline =====")

# Step 1: Remove duplicate records
df_pipeline = df.dropDuplicates()

# Step 2: Fill NULL values in price column with 0
df_pipeline = df_pipeline.na.fill({"price": 0})

# Step 3: Group by store_id and calculate total revenue
final_result = (
    df_pipeline
    .groupBy("store_id")
    .agg(sum("price").alias("Total_Revenue"))
)

# Display Result
final_result.show()

spark.stop()