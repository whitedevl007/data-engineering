import logging
from datetime import datetime

from cassandra.auth import PlainTextAuthenticator
from cassandra.cluster import Cluster

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col

def create_keyspace(session):
    #create keyspace here

def create_table(session):
    #create table here

def insert_data(session, **kwargs):
    #insertion here

def create_spark_connection():
    try:
       s_conn = SparkSession.builder \
            .appName('SparkDataStreaming') \
            .config('spark.jars.packages', "com.datastax.spark:spark-cassandra-connector_2.12:3.5.0,"
                    "org.apache.spark:spark-sql-kafka-0.-10_2.12:3.5.1") \
            .config('spark.cassandra.connection.host', 'localhost') \
            .getOrCreate()
       
       s_conn.sparkContext.setLogLevel("ERROR")
       logging.info("Spark connection created successfully!")
    except Exception as e:
        logging.error("Couldn't create the spark session due to exception {}")

    return s_conn

def create_cassandra_connection():
    #creating cassandra connection

if __name__ == "__main__":
    spark_conn = create_spark_connection()