from sklearn.feature_extraction.text import CountVectorizer

v=CountVectorizer(binary=False)
docs=['the cat is out of the bag','the dog is the biggest']
bow=v.fit_transform(docs)

print(bow.toarray())
print(v.vocabulary_)#で単語とインデックがわかる
