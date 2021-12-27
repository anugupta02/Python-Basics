import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('played', pos="v"))
print(lemmatizer.lemmatize('playing', pos="n"))
print(lemmatizer.lemmatize('playing', pos="a"))
print(lemmatizer.lemmatize('playing', pos="r"))
print(lemmatizer.lemmatize('stones', pos="v"))


import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
print(stemmer.stem('stones'))   #Stemmer removes es in word
print(stemmer.stem('speaking'))
print(stemmer.stem('bedroom'))
print(stemmer.stem('jaked'))
print(stemmer.stem('lisa'))
print(stemmer.stem('purpled'))
print('----------------------')
print(lemmatizer.lemmatize('stones'))  #lemmatizer removes 

#lemma is the base form of all its inflectional forms, whereas a stem isn’t.
#The stem can be the same for the inflectional forms of different lemmas.
#The same lemma can correspond to forms with different stems
'''
Stemming: there are different algorithms that can be used in the stemming process, 
but the most common in English is Porter stemmer. 
The rules contained in this algorithm are divided in five different phases numbered from 1 to 5. 
The purpose of these rules is to reduce the words to the root.
Lemmatization: the key to this methodology is linguistics. To extract the proper lemma, 
it is necessary to look at the morphological analysis of each word. 
This requires having dictionaries for every language to provide that kind of analysis.
'''

print(lemmatizer.lemmatize('speaking'))
print(lemmatizer.lemmatize('bedrooms'))
print(lemmatizer.lemmatize('jaked'))
print(lemmatizer.lemmatize('lisa'))
print(lemmatizer.lemmatize('purple'))

import nltk
from nltk.tokenize import PunkSentenceTokenizer

document = 'Whether Anu you\'re new to'
sentences = nltk.sent_tokenize(document)
for sent in sentences:
    print(nltk.pos_tag(nltk.word_tokenize(sent)))
	
	
import nltk
#from nltk.corpus

from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.corpus import stopwords
url='http://www.php.net'
content=urllib.request.urlopen(url)
con =BeautifulSoup(content, 'html.parser')
#print(text)
tokens = [t for t in text.split()] #split removes spaces in between words
freq = nltk.FreqDist(tokens)
#sw=set(stopwords.words('english')
#print(len(sw))--> iska output 179 ayega joh is,this,that,was,etc inn saab verbs ke counts hai
for key,val in freq.items():  #key and val ko return krta hai
    #if key not in sw:
	print(key,':',val)
	

'''Twitter Analysis Tommorow:
Prerequisites are:
pip install tweety
pip install textblob
https://developer.twitter.com/en/application/in-review
'''

