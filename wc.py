from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt

# カレントディレクトリの設定
d = path.dirname(__file__)

# WordCloudに渡す文章
text = "This article is about the sandwich. For the meat served as part of such a sandwich, see Patty. For other uses, see Hamburger (disambiguation).Hamburger RedDot Burger.jpg Hamburger with french fries and a beer Course Main course Place of origin United States or Germany disputed Created by Multiple claims (see text) Serving temperature Hot Main ingredients Ground meat, bread Cookbook: Hamburger Media: Hamburger A hamburger, beefburger or burger is a sandwich consisting of one or more cooked patties of ground meat, usually beef, placed inside a sliced bread roll or bun. The patty may be pan fried, grilled, or flame broiled. Hamburgers are often served with cheese, lettuce, tomato, onion, pickles, bacon, or chiles; condiments such as ketchup, mayonnaise, mustard, relish, or special sauce and are frequently placed on sesame seed buns. A hamburger topped with cheese is called a cheeseburger. The term burger can also be applied to the meat patty on its own, especially in the United Kingdom, where the term patty is rarely used, or the term can even refer simply to ground beef. The term may be prefixed with the type of meat or meat substitute used, as in turkey burger, bison burger, or veggie burger Hamburgers are sold at fast-food restaurants, diners, and specialty and high-end restaurants (where burgers may sell for several times the cost of a fast-food burger, but may be one of the cheaper options on the menu). There are many international and regional variations of the hamburger."

# 元画像の指定
alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

# WordCloudのパラメーター設定
wc = WordCloud(
               background_color = "white",
               max_words        = 2000,
               mask             = alice_mask,
              )

# WordCloudの実行
wc.generate(text)

# 生成した画像をファイルとして出力
wc.to_file(path.join(d, "alice.png"))