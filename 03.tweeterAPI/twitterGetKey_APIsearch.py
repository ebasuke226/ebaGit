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
for tweet in api.search(q="日立製作所",lang='ja',count=10000):
    tweet_data.append([tweet.id,tweet.created_at,tweet.text.replace('\n',''),tweet.favorite_count,tweet.retweet_count])

#csv出力
with open('tweets_hitachi.csv', 'w',newline='',encoding='utf-8_sig') as f:
    writer = csv.writer(f)
    writer.writerow(["Id","Timestamp","Tweet","Favorite","RT"])
#    tweet_data = tweet_data.encode('cp932', "ignore")　#一度cp932に変換するがエラーは無視する
    writer.writerows(tweet_data)  #書き込み
pass

data = pd.DataFrame(tweet_data)
data.columns = ['Id',' Timestamp', 'Tweet', 'Favorite', 'RT']
