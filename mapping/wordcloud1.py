import hashlib
import pandas as pd
from wordcloud import WordCloud
geo_date = pd.read_excel(r"../data/geo_data.xlsx")

print(geo_date)

words = ','.join(x for x in geo_date['city'] if x != []) # 筛选出非空列表值
wc = WordCloud(
    background_color="green",  # 背景颜色 “ green ” 绿色
    max_words=100,  # 显示最大词数
    font_path='./fonts/simhei.ttf',  # 显示中文
    min_font_size=5,
    max_font_size=100,
    width=500
)
x = wc.generate(words)
x.to_file('../data/geo_date.png')

