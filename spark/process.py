# spark/process.py
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CO2 Processor").getOrCreate()

# Charger les données CSV
df = spark.read.csv("/data/co2.csv", header=True, inferSchema=True)
df_clean = df.dropna(subset=["lat", "lon", "taux_co2"])

# Sauvegarde dans PostgreSQL
df_clean.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://db:5432/co2db") \
    .option("dbtable", "co2_data") \
    .option("user", "user") \
    .option("password", "pass") \
    .option("driver", "org.postgresql.Driver") \
    .save()
