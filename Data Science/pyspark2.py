from pyspark.sql import SQLContext
url = "adult.csv"
from pyspark import SparkFiles

sc.addFile(url)
sqlContext = SQLContext(sc)

'''
Registers a lambda function as a UDF so it can be used in SQL statements. 
source code. 
inferSchema(self, rdd) Infer and apply a schema to an RDD of Rows.
Infer and apply a schema to an RDD of Rows. We peek at the first row of the RDD to determine the fields' names and types. 
Nested collections are supported, which include array, dict, list, Row, tuple, namedtuple, or object.
InferSchema ko True rkha toh voh har ek words ko apne datatype ke hisaab se batayega
aur agar False rkha hai toh by default String hi batayega har ek element ko
'''

df = sqlContext.read.csv(SparkFiles.get("adult.csv"),header=True,inferSchema=True)
df.printSchema()
df.show(2)
df_string = sqlContext.read.csv(SparkFiles.get("adult.csv"), header=True, inferSchema=False)
df_string.printSchema()


#Lambda is a function which can take any number of arguments, 
#but can only have one expression. 

#To convert the continuous variable in the right format,
#you can use recast the columns. You can use withColumn 
#to tell Spark which column to operate the transformation.
# Import all from `sql.types`
from pyspark.sql.types import *

# Write a custom function to convert the data type of
#DataFrame columns
def convertColumn(df, names, newType):
    for name in names: 
        df = df.withColumn(name, df[name].cast(newType))
    return df 
# List of continuous features
CONTI_FEATURES  = ['age', 'fnlwgt','capital-gain', 'educational-num','capital-loss', 'hours-per-week']
# Convert the type
df_string = convertColumn(df_string, CONTI_FEATURES,FloatType())
# Check the dataset
df_string.printSchema()

from pyspark.ml.feature import StringIndexer
#stringIndexer = StringIndexer(inputCol="label", outputCol="newlabel")
#model = stringIndexer.fit(df)
#df = model.transform(df)
df.printSchema()

df.select('age','fnlwgt','education').show(5)	
#df.select('*').show()
#df.select('*').show()
df.groupBy("education").count().sort("count",ascending=False).show()
df.describe()
df.describe('capital-gain').show()
#df.select('label').show()
#df.crosstab('age', 'educational').sort("age-label").show()

df.drop('education-num').columns
df.filter(df.age > 40).count()
#df.groupby('marital').agg({'capital-gain': 'mean'}).show()

df.filter(df.age < 40).count()
df.groupby('age').agg({'capital-gain': 'mean'}).show()
print(df)

from pyspark.sql.functions import *
# 1 Select the column
age_square1 = df.select(col("age")**2)  #age_square ek new column add ho jaye
# 2 Apply the transformation and add it to the DataFrame
df = df.withColumn("age_square", col("age")**2)
df.printSchema()

COLUMNS = ['age', 'age_square', 'workclass', 'fnlwgt', 'education', 
           'marital',
           'occupation', 'relationship', 'race', 'sex', 'capital_gain', 
           'capital_loss',
           'hours_week', 'native_country', 'label']
		   
COLUMNS = ['age', 'age_square', 'workclass', 'Private', 'fnlwgt', 
           'education','occupation']
df = df.select(COLUMNS)
#print(df.first())
#print(df.last())
print(df.show(5))

print(df.select('native_country').show(5))
df.filter(df.native_country == 'Holand-Netherlands').count()
df.groupby('native_country').agg({'native_country': 'count'}).sort(asc("count(native_country)")).show()

df_remove = df.filter(df.native_country !='Holand-Netherlands').show()

StringIndexer(inputCol="workclass", outputCol="workclass_encoded")
df.drop('education_num').columns

StringIndexer(inputCol="workclass", outputCol="workclass_encoded")

#Fit the data and transform it
model = stringIndexer.fit(df)		
indexed = model.transform(df)