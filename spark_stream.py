from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("NetSageSpark").getOrCreate()

df = spark.readStream.format("kafka")     .option("kafka.bootstrap.servers", "kafka:9092")     .option("subscribe", "netflow").load()

query = df.writeStream.outputMode("append").format("console").start()
query.awaitTermination()
