import csv
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import tweepy
from bs4 import BeautifulSoup
from collections import Counter, defaultdict
from datetime import datetime
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud

CK = 'XXXXXXXXXXXXXXXXXXXXXXXXX'                             # Consumer Key
CS = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'    # Consumer Secret
AT = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'    # Access Token
AS = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'         # Accesss Token Secert

auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)
api = tweepy.API(auth)

#ツイート取得
tweet_data = []
for tweet in tweepy.Cursor(api.user_timeline,screen_name = "kawasaki_f",exclude_replies = True).items():
    tweet_data.append([tweet.id,tweet.created_at,tweet.text.replace('\n',''),tweet.favorite_count,tweet.retweet_count])

#csv出力
with open('tweets_furonta.csv', 'w',newline='',encoding='utf-8_sig') as f:
    writer = csv.writer(f)
    writer.writerow(["Id","Timestamp","Tweet","Favorite","RT"])
#    tweet_data = tweet_data.encode('cp932', "ignore")　#一度cp932に変換するがエラーは無視する
    writer.writerows(tweet_data)  #書き込み
pass

data = pd.DataFrame(tweet_data)
data.columns = ['Id',' Timestamp', 'Tweet', 'Favorite', 'RT']

def counter(texts):
    t = Tokenizer()
    words_count = defaultdict(int)
    words = []
    for text in texts:
        tokens = t.tokenize(text)
        for token in tokens:
            #品詞から名詞だけ抽出
            pos = token.part_of_speech.split(',')[0]
            if pos == '名詞':
                words_count[token.base_form] += 1
                words.append(token.base_form)
    return words_count, words

with open('tweets_ebasuke226_replies.csv','r',encoding="utf-8_sig") as f:
    reader = csv.reader(f, delimiter='\t')
    texts = []
    for row in reader:
        text = row[0].split('http')
        texts.append(text[0])

words_count, words = counter(texts)
text = ' '.join(words)

#word cloud
wordcloud = WordCloud(background_color="white",font_path="FUJIPOP.TTC",width=1024,height=674).generate(text)

plt.figure(figsize=(15,12))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
