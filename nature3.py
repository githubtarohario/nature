from janome.tokenizer import Tokenizer
word_dic={}
tokenizer = Tokenizer()
with open("eiennozero2.txt",encoding="utf-8") as f:
    s = f.read()
    #----------------------
    #NOTE
    #。で区切るなら
    #s1=s.split("。")
    #print(s1[0])
    #---------------------
    for token in tokenizer.tokenize(s):
        hinshi=token.part_of_speech
        word=token.surface
        if hinshi.find("名詞") < 0:continue#名詞でないなら
        #print(token.surface,",",token.part_of_speech)
        if not word in word_dic:
            word_dic[word]=0
        word_dic[word]+=1
        #print(word)
for key, value in word_dic.items():
    print(key,",", value)           
