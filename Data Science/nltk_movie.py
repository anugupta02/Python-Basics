import nltk.classify.util
from nltk.classify
import NaiveBayesClassifier
from nltk.corpus
import names

def gender_features(word):
    return {'last_letter': word[-1]}
names = ([name, 'male') for name in names.words
        ('male.txt')]
		+ [(name, 'female')
		   for name in names.words('female.txt')])
featuresetsc=[(gender_features(n) ,g)
              for(n,g) in names]
train_set=featuresets
classifier=nltk.NaiveBayesClassifier.train(train_set)
name=input("Name: ")
print(classifier.classify(gender_features(name)))


'''
Python is case sensitive language
5 Steps of Machine Learning:
Import Data
Import Algorithm
Create Algorithm
Train the Data
Execute the program and we will get Output
'''