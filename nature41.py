from janome.tokenizer import Tokenizer
def analysis(s):
    for token in tokenizer.tokenize(s):
        hinshi=token.part_of_speech
        word=token.surface
        if hinshi.find("名詞") < 0:continue
        if not word in word_dic:
            word_dic[word]=0
        word_dic[word]+=1
    for key, value in word_dic.items():
        print(key,",", value)           
count=0
word_dic={}
tokenizer = Tokenizer()
with open("eiennozero2.txt",encoding="utf-8") as f:
    s = f.read()
    s1=s.split("。")
    for s2 in s1:
        print("count=(",count,")",s2)
        count=count+1
        #analysis(s2)
print("count=",count)    
        #print(word)
