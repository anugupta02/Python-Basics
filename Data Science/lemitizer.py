import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('played', pos="v"))
print(lemmatizer.lemmatize('played', pos="n"))
print(lemmatizer.lemmatize('played', pos="a"))
print(lemmatizer.lemmatize('played', pos="r"))
print(lemmatizer.lemmatize('played', pos="v"))