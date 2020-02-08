import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import preprocessor as p


#text = open("twitter-out.txt","a")
#print(text)

with open('twitter-out.txt', 'r') as tweets:
    text = p.clean(tweets.read())
    #print(text)

stopwords = set(STOPWORDS)
#stopwords.update(["Buttigieg", "Pete Buttigieg", "Bernie Sanders", "Bernie Sander", "Elizabeth Warren", "Joe Biden"])

#Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()