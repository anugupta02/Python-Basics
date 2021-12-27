
import nltk
from nltk.corpus import stopwords
sw=stopwords.words("english")

print(len(sw))
print(sw)

sent="@Python is an #easy to learn!!, powerful $programming and language."
import string
print(string.punctuation)

nsent=[x for x in sent if x not in sw]
nsent=''.join(nsent)  #different words ko join krta hai
print(nsent)

from nltk.tokenize import word_tokenize  #word_tokenize : convert whole sentence to single words
word=word_tokenize(sent)
print(word)


from nltk.tokenize import sent_tokenize
abc="Python is an easy to learn, powerful programming language. It has efficient high-level data? structures and a simple but effective. approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms."
sentence=sent_tokenize(abc)  #sent_tokenize : convert whole paragraph to sentences
print(sentence)

word=[word for words in word if words not in sw]
word=''.join(word)
print(word)

word=[x for x in word if x not in string.punctuation]
word=''.join(word)
print(word)
