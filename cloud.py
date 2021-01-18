from wordcloud import WordCloud
from matplotlib import pyplot as plt
fpath = "C:\Windows\Fonts\ipaexg.ttf"


with open('eiennozero2.txt', mode='rt', encoding='utf-8') as fo:
    cloud_text = fo.read()

word_cloud = WordCloud(font_path=fpath).generate(cloud_text)

plt.imshow(word_cloud)
plt.axis('off')
plt.show()