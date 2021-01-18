from nltk.util import ngrams
from sklearn.feature_extraction.text import CountVectorizer


texts = [ '東京から大阪に行く。', '大阪に行く。',]
cv = CountVectorizer(analyzer='char' , ngram_range=(2,2))
cv.fit_transform(texts)
bow=cv.transform(texts)
print("bow=",bow.toarray())
print("cv=",cv.vocabulary_)
for c2 in cv.vocabulary_.keys():
    print(c2)