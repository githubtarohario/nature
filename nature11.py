#---------------------------------------------------
#nature11.py
#NOTE 管理者権限でancondaを立ち上げ
#C:\Windows\Fonts\ipaexg.ttfをコピーする
#copy ipa*.* C:\Windows\Fonts\
#ipaexg.ttf はあらかじめダウンロードしたもの
#       
#OK
#-----------------------------------------------------
from pathlib import Path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#出力パス設定
image_dir_path = Path('./image')
corpus_dir_path = Path('./corpus')

if not image_dir_path.exists():
    image_dir_path.mkdir(parents=True)

file_name = 'eiennozero2_word_list.txt'#形態解析したテキスト


with open(corpus_dir_path.joinpath(file_name), 'r', encoding='utf-8') as file:
    text = file.readlines()
text = ' '.join(text).replace('\n', '')


# 日本語が使えるように日本語フォントの設定
fpath = 'C:\Windows\Fonts\ipaexg.ttf'



# ストップワードの設定
# ここで設定した単語はWord Cloudに表示されない
stop_words = [u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
              u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した', u'思う', \
              u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て', u'に', u'を', u'は', u'の', u'が', u'と', u'た', u'し', u'で', \
              u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'', u'もの', u'もつ']

print(text)
wordcloud = WordCloud(background_color="white",
                      font_path=fpath,
                      width=900,
                      height=500,
                      stopwords=set(stop_words)).generate(text)

plt.figure(figsize=(10, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout()
plt.savefig(image_dir_path.joinpath(file_name.replace('list.txt', 'cloud.png')).__str__())
plt.show()