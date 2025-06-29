# Databricks notebook source
# MAGIC %md
# MAGIC # DATA ACCESS

# COMMAND ----------

dbutils.fs.ls('abfss://bronze@nyctaxidatalakeneha.dfs.core.windows.net')

# COMMAND ----------

# MAGIC %md
# MAGIC # Data Reading

# COMMAND ----------

# MAGIC %md
# MAGIC **Importing Libraries**

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC **Reading CSV DATA**

# COMMAND ----------

# MAGIC %md
# MAGIC **Trip Type Data**

# COMMAND ----------

df_trip_type = spark.read.format('csv')\
    .option('header', 'true')\
    .option('inferSchema', 'true')\
    .load('abfss://bronze@nyctaxidatalakeneha.dfs.core.windows.net/trip_type/trip_type.csv')


# COMMAND ----------

df_trip_type.display()

# COMMAND ----------

# MAGIC %md
# MAGIC **Trip Zone Data**

# COMMAND ----------

df_trip_zone = spark.read.format('csv')\
    .option('header', 'true')\
    .option('inferSchema', 'true')\
.load('abfss://bronze@nyctaxidatalakeneha.dfs.core.windows.net/trip_zone/taxi_zone_lookup.csv')


# COMMAND ----------

df_trip_zone.display()

# COMMAND ----------

# MAGIC %md
# MAGIC **Trip Data**

# COMMAND ----------

myschema = '''
                VendorID BIGINT,
                lpep_pickup_datetime TIMESTAMP,
                lpep_dropoff_datetime TIMESTAMP,
                store_and_fwd_flag STRING,
                RatecodeID BIGINT,
                PULocationID BIGINT,
                DOLocationID BIGINT,
                passenger_count BIGINT,
                trip_distance DOUBLE,
                fare_amount DOUBLE,
                extra DOUBLE,
                mta_tax DOUBLE,
                tip_amount DOUBLE,
                tolls_amount DOUBLE,
                ehail_fee DOUBLE,
                improvement_surcharge DOUBLE,
                total_amount DOUBLE,
                payment_type BIGINT,
                trip_type BIGINT,
                congestion_surcharge DOUBLE
          '''


# COMMAND ----------

df_trip = spark.read.format('parquet')\
    .option('header', 'true')\
    .schema(myschema)\
    .option('recursiveFileLookup', 'true')\
    .load('abfss://bronze@nyctaxidatalakeneha.dfs.core.windows.net/trips2023data')

# COMMAND ----------

df_trip.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # DATA TRANSFORMATION

# COMMAND ----------

# MAGIC %md
# MAGIC **Taxi Trip Type**

# COMMAND ----------

df_trip_type.display()

# COMMAND ----------

df_trip_type = df_trip_type.withColumnRenamed('description', 'trip_description')
df_trip_type.display()

# COMMAND ----------

df_trip_type.write.format('parquet').mode('overwrite').option('path', 'abfss://silver@nyctaxidatalakeneha.dfs.core.windows.net/trip_type').save()

# COMMAND ----------

# MAGIC %md
# MAGIC **Taxi Trip Zone**

# COMMAND ----------

df_trip_zone.display()

# COMMAND ----------

df_trip_zone = df_trip_zone \
    .withColumn('zone1', split(col('Zone'), '/').getItem(0)) \
    .withColumn('zone2', split(col('Zone'), '/').getItem(1))


# COMMAND ----------

df_trip_zone.display()

# COMMAND ----------

df_trip_zone.write.format('parquet').mode('append').option('path', 'abfss://silver@nyctaxidatalakeneha.dfs.core.windows.net/trip_zone').save()

# COMMAND ----------

# MAGIC %md
# MAGIC **Trip Data**

# COMMAND ----------

df_trip.display()

# COMMAND ----------

df_trip = df_trip.withColumn('trip_date',to_date('lpep_pickup_datetime'))\
                 .withColumn('trip_year',year('lpep_pickup_datetime'))\
                 .withColumn('trip_month',month('lpep_pickup_datetime'))
                 

# COMMAND ----------

df_trip.display()

# COMMAND ----------

df_trip = df_trip.select('VendorID', 'PULocationID', 'DOLocationID', 'fare_amount', 'total_amount')

# COMMAND ----------

df_trip.display()

# COMMAND ----------

df_trip.write.format('parquet').mode('append').option('path', 'abfss://silver@nyctaxidatalakeneha.dfs.core.windows.net/trips2023data').save()

# COMMAND ----------

# MAGIC %md
# MAGIC # Analysis

# COMMAND ----------

display(df_trip)