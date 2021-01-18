import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
t=Tokenizer(wakati=True)
v=CountVectorizer(tokenizer=t.tokenize)
docs=["欅坂はアイドルグループです。","欅坂は坂道です。欅坂は東京です。"]
print("docs[0]",docs[0])
print("docs[1]",docs[1])

bow=v.fit_transform(docs)
vocab=v.get_feature_names()
print(pd.DataFrame(bow.toarray(),columns=vocab))
