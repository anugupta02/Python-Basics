import nltk.classify.util
from nltk.classify 
import NaiveBayesClassifier
def word_feats(words):
    return dict([(words,False)])
	
positive_vocab = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good',
                  'nice', 'great', ':)','better','best','excellent']
negative_vocab = ['bad','terrible','useless','hate',':(','not']
neutral_vocab  = ['movie','the','sound','was','is','actor','did','know','words']


positive_features = [(word_feats(pos),'pos')]
                     for pos in positive_vocab]
					 
#print(positive_features)
					 
negative_features = [(word_feats(neg),'neg')]
                     for neg in negative_vocab]
neutral_features = [(word_feats(neu),'neu')]
                     for neu in neutral_vocab]

nb = NaiveBayesClassifier.train(train_set)					 

#Predict
neg = 0
pos = 0
neu = 0
sentence="Awesome movie Sound is not good but still its good in feature"
sentence=sentence.lower()
words=sentence.split()
for word in words:
    classResult = nb.classify(word_feats(word))
	#print(word,classResult)
	
	if classResult == 'neg':
	    neg = neg + 1
	if classResult == 'pos':
	    pos = pos + 1
	if classResult == 'neu':
	    neu = neu + 1

#print(words)
#print(pos)

print('Neu : ' +str(float(neu)/len(word)))
print('Positive : ' +str(float(pos)/len(word)))
print('Negative : ' +str(float(neg)/len(word)))

if neg>pos and neg>neu:
    print('movie is not good')
elif pos>neg and pos>neu:
      print('movie is good')
else:
    print('One time you can see this movie')