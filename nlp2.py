from nltk.corpus import gutenberg
#for POS (parts of speech)
from nltk.tag import pos_tag_sents
from nltk import word_tokenize

emma = gutenberg.words('austen-emma.txt')
emma_tokens = word_tokenize('austen-emma.txt')

emma_tagged = pos_tag_sents(emma_tokens)

JJ_count = 0
NN_count = 0

for words in emma_tagged:
	for pair in words:
		tag = pair[1]
		if tag == 'JJ':
			JJ_count += 1
		elif tag == 'NN':
			NN_count += 1

print ('Total number of adjectives = ', JJ_count)
print ('Total number of nouns = ', NN_count)

