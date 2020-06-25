from pyspark.sql import SparkSession
spark = SparkSession\
.builder\
.getOrCreate()

print("Testing simple count")

def spark_f(n_rows):
    # The Spark code will execute on the Azure Databricks cluster...
    n = spark.range(n_rows).count()
    return n

def python_f(n_rows):
    n = len(range(n_rows))
    return n

spark_count = spark_f(10000)
python_count = python_f(9999)

print(spark_count)
print(python_count)

#trying some stuff in release
