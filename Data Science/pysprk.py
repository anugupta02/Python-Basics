#import pyspark
from pyspark import SparkContext
sc =SparkContext('local','appname')

nums= sc.parallelize([13,2,3,4,5,6,7,8,9])
print(nums)

print(nums.take(5))

squared = nums.map(lambda x: x*x).collect()
for num in squared:
    print('%i ' % (num))
	
from pyspark.sql import Row
from pyspark.sql import SQLContext
#from  pyspark import SparkContext

#sc.stop()
#sc=SparkContext()
sqlContext = SQLContext(sc)

list_p=[('John',19),('Smith',29),('Adam',35),('Henry',50)]
print(list_p)  #list_p is 2 - Dimentional data

'''
Build a RDD(Resilient Distributed Dataset):
Resilient Distributed Datasets:-
It is an immutable distributed collection of objects. 
Each dataset in RDD is divided into logical partitions, 
which may be computed on different nodes of the cluster. 
RDDs can contain any type of Python, Java, or Scala objects, 
including user-defined classes.
'''

rdd = sc.parallelize(list_p)
ppl=rdd.map(lambda x: Row(name=x[0], age=int(x[1])))
print(ppl)

#Create a DataFrame context
#sqlContext.createDataFrame(ppl)
#list_p = [('John',19),('Smith',29),('Adam',35),('Henry',50)]
#rdd = sc.parallelize(list_p)
#ppl = rdd.map(lambda x: Row(name=x[0], age=int(x[1])))
DF_ppl = sqlContext.createDataFrame(ppl)
DF_ppl.printSchema()
DF_ppl.show()


