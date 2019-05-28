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

#auth = tweepy.OAuthHandler(CK,CS)
#auth.set_access_token(AT,AS)
#api = tweepy.API(auth)

#ツイート取得
test2 = []

for tweet in tweepy.Cursor(api.search, q = 'TOYOTA').items():
    test2.append([tweet.id,tweet.created_at,tweet.text.replace('\n',''),tweet.favorite_count,tweet.retweet_count])

data2 = pd.DataFrame(test2)
data2.columns = ['Id',' Timestamp', 'Tweet', 'Favorite', 'RT']

#csv出力
with open('tweets_20180325_TOYOTA.csv', 'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Id","Timestamp","Tweet","Favorite","RT"])
    writer.writerows(test2)  #書き込み
pass
