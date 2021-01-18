from nltk.util import ngrams
from sklearn.feature_extraction.text import CountVectorizer



texts = [
    '東京から大阪に行く',
    '大阪から東京に行く',
]





cv = CountVectorizer(analyzer='char' , ngram_range=(3,3))

cv.fit_transform(texts)
bow=cv.transform(texts)
print(bow.toarray())
print(cv.vocabulary_)
#print(cv.get_feature_names())
#print(matrix.todense())










