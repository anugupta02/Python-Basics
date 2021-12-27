class TwitterCleient():
    def __init__(self):
        consumer_key = 'cSjBuDXz'
		
		
		
		
		
	
	
	
	
	
	def clean_tweet(self, tweet):
	    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|
		                        (\w+:\/\/\S+)", " ", tweet).split())
	
	'''
	Polarity is float which lies in the range of [-1,1] where 1 
	means positive statement and -1 means a negative statement. 
	Subjective sentences generally refer to personal opinion, emotion or 
	judgment whereas objective refers to factual information. 
	Subjectivity is also a float which lies in the range of [0,1].
	'''
	
	'''
	Sentiment Analysis is the process of 'computationally' determining 
	whether a piece of writing is positive, negative or neutral. 
	It's also known as opinion mining, deriving the opinion or attitude 
	of a speaker.
	'''
	
	'''
	Sentiment Analysis is a technique used in text mining. 
	Twitter Sentiment Analysis may, therefore, be described as a 
	text mining technique for analyzing the underlying sentiment of 
	a text message, i.e., a tweet. Twitter sentiment or opinion expressed 
	through it may be positive, negative or neutral.
	'''
	
	def get_tweet_sentiment(self,tweet):
	    analysis = TextBlob(self.clean_tweet(tweet))
		#set sentiment
		if analysis.sentiment.polarity > 0:
		   return 'positive'
		elif analysis.sentiment.polarity == 0:
		   return 'neutral'
		else:
		    return 'negative'
		
		'''
		Main function to fetch tweets and parse them.'''
		
		#empty list to store parsed tweets
		tweets = []
		 
		try:
		   #call twitter api to fetch tweets
		   fetched_tweets = self.api.search(q=query,count=count)
		   
		   #parsing tweets one by one
		   for tweet in fetched_tweets:
		       #empty dictionary to store required params of a tweets
	           parsed_tweet = {}
			   
			   #saving text of tweets
			   parsed_tweet['text'] = tweet.text
	#text mein twitter handle and 
	#sentiment mein uss twitter handle ki value means tweets ayenge
	
	