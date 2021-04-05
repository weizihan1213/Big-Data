# Command: spark-submit spark_std.py
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import SQLContext

# Spark set-up
conf = SparkConf()
conf.setAppName("Purchase App")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

# uncomment the sc.setLoglevel line, when your program works fine. 
# Run the program again to take the screenshot.
sc.setLogLevel("WARN")

# Upload data file in Hadoop and provide its path in textFile function
rdd = sc.textFile("/user/spark/sales.txt")

# Add a few lines of code here to split 
# the attributes in each line, pick only required attributes,
# change type of attributes if needed.
rdd = rdd.map(lambda x: x.split('\t'))
sales = rdd.map(lambda x: Row(city=x[2], sale=float(x[4])))

# function for formatting the element of RDD
def update(x):
    x[1] = round(x[1], 2)
    x[2] = round(x[2], 3)
    return x

# Add code to convert RDD to dataframe
schemaSales = sales.toDF()

# create SQL table from data frame.
schemaSales.registerTempTable("sales")


sqlContext = SQLContext(sc)
# Write query using sqlContext.sql() function
ave_and_sd = sqlContext.sql("SELECT city, AVG(sale), STDDEV(sale) FROM sales GROUP BY city")
rdd = ave_and_sd.rdd.map(list)
out = rdd.map(update)
out = out.toLocalIterator()
# You may convert SQL dataframe in RDD
# and use it for pretty formatting as mentioned below
# city\t(average sale with 2 digits after decimal)\t(standard deviation in sale with 3 digits after decimal) 
# For example:
# Las Vegas	1200.56	23.321

# Then you can get the output in out variable display the results.	
for item in out:
	print (item[0]+':\t'+str(item[1])+', '+str(item[2]))



