from nltk.corpus import gutenberg
from gensim.models import Word2Vec
#for POS (parts of speech)
from nltk.tag import pos_tag_sents

g = Word2Vec(gutenberg.raw())
#g_tokens = g.tokenized('positive_tweets.json')

g_tagged = pos_tag_sents(g)
g_len = len(g_tagged)
print(g_len)

#JJ_count = 0
#NN_count = 0

#for tweet in tweets_tagged:
#	for pair in tweet:
#		tag = pair[1]
#		if tag == 'JJ':
#			JJ_count += 1
#		elif tag == 'NN':
#			NN_count += 1

#print ('Total number of adjectives = ', JJ_count)
#print ('Total number of nouns = ', NN_count)

