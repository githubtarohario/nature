from janome.tokenizer import Tokenizer
import collections
t = Tokenizer()
s = 'これは、ペンです。あれは、本です。'

for token in t.tokenize(s):
    print(token)
c = collections.Counter(t.tokenize(s, wakati=True))
print(c)
