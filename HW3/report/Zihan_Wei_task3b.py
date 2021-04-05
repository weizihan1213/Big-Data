#Command: spark-submit spark_wc.py
from pyspark import SparkConf, SparkContext

#Spark set-up
conf = SparkConf()
conf.setAppName("Word count App")
sc   = SparkContext(conf=conf)

#uncomment the sc.setLoglevel line, when your program works fine. 
#Run the program again to take the screenshot.
sc.setLogLevel("WARN")

# Upload data file in Hadoop and provide its path in textFile function
rdd  = sc.textFile("/user/spark/words.txt")
rdd  = rdd.flatMap(lambda x: x.split(' '))
rdd	 = rdd.map(lambda x: (x, 1))
# Add few lines of code below
def trim_words(x):
	end_chars = ["'", ',', '.', '?', '!', '"', ' ', ';', ]
	x = list(x)
	if len(x[0]) > 0:
		while x[0][-1] in end_chars:
			x[0] = x[0][:-1]
		while x[0][0] in end_chars:
		  x[0] = x[0][1:]
		x[0] = x[0].lower()
	x = tuple(x)
	return x

rdd = rdd.map(trim_words)
rdd  = rdd.reduceByKey(lambda x,y: x+y)
# Add your code below
out = rdd.takeOrdered(10, key = lambda x: -x[1])
#
# you may store top 10 results in 'out' variable
# and use it to display as mentioned below.
for item in out:
	print (item[0],'\t:\t',str(item[1]))

