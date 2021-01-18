# すでに３つの文章が形態素解析済みであるとします。
# morphemesには分かち書きされたものが入っています。
morphemes =  [
    '私 は 私 の こと が 好き な あなた が 好き です',
    '私 は ラーメン が 好き です',
]             
             
             
             

# 単語に数値を割り当てます。
word2id = {} # {単語: ID}
for line in morphemes:
    for word in line.split():
        if word in word2id:
#            print(word,"---",word2id)
            continue
        word2id[word] = len(word2id)
print(word2id)
# Bag of Wordsを作る
bow_set = []
for line in morphemes:
    bow = [0] * len(word2id)
    for word in line.split():
        try:
            bow[word2id[word]] += 1
        except:
            pass
    bow_set.append(bow)
print(*bow_set, sep="\n")
print(bow_set)
