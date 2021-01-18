from wordcloud import WordCloud

import pandas as pd

from janome.tokenizer import Tokenizer

import matplotlib.pyplot as plt
## データ読み込み
#df = pd.read_csv('sample.csv', header=None)
df = pd.read_csv('gingatetsudono_yoru-utf.txt', header=None)

## タイトルを付与
df.colums = ['sentences']

## 関数群の定義
def get_nouns(sentence, noun_list):
    for token in t.tokenize(sentence):
        split_token = token.part_of_speech.split(',')
        ## 一般名詞を抽出
        if split_token[0] == '名詞' and split_token[1] == '一般':
            noun_list.append(token.surface)

def depict_word_cloud(noun_list):
    ## 名詞リストの要素を空白区切りにする(word_cloudの仕様)
    noun_space = ' '.join(map(str, noun_list))
    ## word cloudの設定(フォントの設定)
    wc = WordCloud(background_color="white", font_path=r"C:/WINDOWS/Fonts/msgothic.ttc", width=300,height=300)
    wc.generate(noun_space)
    ## 出力画像の大きさの指定
    plt.figure(figsize=(5,5))
    ## 目盛りの削除
    plt.tick_params(labelbottom=False,
                    labelleft=False,
                    labelright=False,
                    labeltop=False,
                   length=0)
    ## word cloudの表示
    plt.imshow(wc)
    plt.show()

    
    
 ## 形態素解析の準備
t = Tokenizer()

noun_list = []
for sentence in list(df['sentences']):
    get_nouns(sentence, noun_list)

depict_word_cloud(noun_list)   