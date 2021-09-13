# -*- coding: utf-8 -*-
import MeCab
import matplotlib.pyplot as plt
import csv
from wordcloud import WordCloud

dfile = "test.txt"

fname = r"'" + dfile + "'"
fname = fname.replace("'","")

mecab = MeCab.Tagger("-Owakati")

words = []

with open(fname, 'r', encoding="utf-8") as f:

	reader = f.readline()

	while reader:

		node = mecab.parseToNode(reader)

		while node:
			word_type = node.feature.split(",")[0]

			if word_type in ["名詞", "動詞", "形容詞", "副詞"]:

				words.append(node.surface)

			node = node.next

		reader = f.readline()

font_path = "NotoSansMonoCJKjp-Regular.otf"

txt = "	".join(words)

stop_words = ['https','t','co','自民','し','w','そう', 'ない', 'いる', 'する', 'まま', 'よう', 'てる', 'なる', 'こと', 'もう', 'いい', 'ある', 'ゆく', 'れる', 'ん', 'の']

wordcloud = WordCloud(background_color="white", font_path=font_path, stopwords=set(stop_words),
	width=800, height=600).generate(txt)

wordcloud.to_file('./wordcloud.png')