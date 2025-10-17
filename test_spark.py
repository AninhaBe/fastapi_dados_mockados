from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TestSpark") \
    .master("local[*]") \
    .getOrCreate()

data = [("Ana", 22), ("Izabelle", 20)]
df = spark.createDataFrame(data, ["nome", "idade"])
df.show()

spark.stop()
