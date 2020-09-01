from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.flume import FlumeUtils

conf = SparkConf().setAppName("Test").setMaster("local")
sc = SparkContext.getOrCreate(conf)

ssc = StreamingContext(sc,2)
flumeStream = FlumeUtils.createStream(ssc, "localhost", 3333)
#tweets =flumeStream.map(lambda x: x.getBytes)
#tweets.pprint()
flumeStream.pprint()

ssc.start()
ssc.awaitTermination()
