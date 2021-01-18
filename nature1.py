from janome.tokenizer import Tokenizer
tokenizer = Tokenizer()
sentence = "私の好きな作家は東野圭吾です"
for token in tokenizer.tokenize(sentence):
    print("surface=",token.surface)#表層
    print("token.part_of_speech=",token.part_of_speech)#品詞

