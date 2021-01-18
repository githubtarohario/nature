from sklearn.feature_extraction.text import CountVectorizer
v=CountVectorizer(binary=True)
v=CountVectorizer(binary=True)
docs=['the cat dog is cat','the dog is big']
bow=v.fit_transform(docs)
print("v1=",v.vocabulary_)
print("v2=",bow.toarray())
