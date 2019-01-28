from gensim.models import Word2Vec
from nltk.corpus import brown, movie_reviews, treebank
b = Word2Vec(brown.sents())
mr = Word2Vec(movie_reviews.sents())
t = Word2Vec(treebank.sents())

print(b)

x = b.wv.most_similar('money', topn=5)
mr.wv.most_similar('money', topn=5)
t.wv.most_similar('money', topn=5)

print(x)

#b.wv.most_similar('great', topn=5)
#mr.wv.most_similar('great', topn=5)
#t.wv.most_similar('great', topn=5)

#b.wv.most_similar('company', topn=5)
#mr.wv.most_similar('company', topn=5)
#t.wv.most_similar('company', topn=5)
