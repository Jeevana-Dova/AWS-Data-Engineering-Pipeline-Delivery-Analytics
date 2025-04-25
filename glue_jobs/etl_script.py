# Script developed in AWS Glue Console using PySpark
# This is a documented copy for GitHub reference

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import when
from pyspark.sql.functions import col

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load raw CSV
df = spark.read.option("header", "true").csv("s3://deliveryeficiencyanalysisdata/raw/train.csv")
# Print schema and preview rows to debug
df.printSchema()
df.show(5)

# Safely access complex column name using backticks
df_cleaned = df.withColumn("On_Time", when(col("`Reached.on.Time_Y.N`") == "1", "Yes").otherwise("No"))

# S3 as Parquet
df_cleaned.write.mode("overwrite").parquet("s3://deliveryeficiencyanalysisdata/processed/")

job.commit()
