import nltk
from nltk.corpus import wordnet

syn = wordnet.synsets('good')
#print(syn)
print(syn[2].defination())
print(syn[2].examples())

'''
from nltk.corpus import wordnet
syn = wordnet.synsets('bad')
#print(syn)
print(syn[1].defination())
print(syn[1].examples())

from nltk.corpus import wordnet
synonyms = []
for syn in wordnet.synsets('sorry'):  #synsets is for fetvhing synonyms
    for lemma in syn.lemmas():
	    #print(lemma)
		synonyms.append(lemma.name())
print(synonyms)


from nltk.corpus import wordnet
antonyms = []
for syn in wordnet.synsets('bad'):  #synsets is for fetvhing synonyms
    for l in syn.lemmas():
	    if l.antonyms():
		   antonyms.append(l.antonyms()[0].name())
print(antonyms)

'''