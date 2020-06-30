from pyspark.sql import SparkSession
spark = SparkSession\
.builder\
.getOrCreate()

def spark_f(n_rows):
    # The Spark code will execute on the Azure Databricks cluster...
    n = spark.range(n_rows).count()
    return n

def python_f(n_rows):
    n = len(range(n_rows))
    return n

print("Hi Microsoft team! Morning test")

