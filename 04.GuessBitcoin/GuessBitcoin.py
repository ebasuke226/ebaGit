import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from pandas import DataFrame

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import mean_squared_error
import math

# 終値情報を持つcsvから価格を得ます
def importData():
    btc_price = pd.read_csv('coindesk-bpi-USD-close_data-2018-03-14_2018-03-21.csv')
    btc_price = btc_price[['Close Price']]
    data = np.array(btc_price)
    return data

data = importData()

# ここでは15時間前までを見るものとします
days_ago = 15

X = np.zeros((len(data), days_ago))

# 時間による推移を見て、そこから偏差を学習できるようにします
for i in range(0, days_ago):
    X[i:len(data), i] = data[0:len(data) - i, 0]

Y =X[:,0]
X = X[:,1:]
# 予測する時間を指定します
predict_time = 1

#学習では、50~2800行目を使うものとします。これは情報の偏りを防ぐためのものであり、全体でも構いません
#train_x = X[50:2800,:]
#train_y = Y[50:2800]

# 残りの全てをテストデータとします
test_x = X[0:len(X)-predict_time,:]
test_y = Y[0:len(Y)-predict_time]

#TODO: LinearRegression を使用して線形回帰モデルで学習させよう。
model = linear_model.LinearRegression()
model.fit(X,Y)

#TODO: pred_y に対して、テストデータを使用して学習結果を代入しましょう
pred_y = model.predict(test_x)

# 予測結果を出力します
result = pd.DataFrame(pred_y)
result.columns = ['pred_y']
result['test_y'] = test_y

# Plot
plt.plot(range(0,len(result)), test_y, label='Actual price', color='blue')
plt.plot(range(0,len(result)), pred_y, label='Predicted price', color='red')
plt.xlabel('Hours')
plt.ylabel('Price ($)')
plt.title('Bitcoin Price')
plt.grid(True)
plt.legend()

plt.show()

# Plot拡大
#plt.plot(range(0,len(result[700:800])), test_y[700:800], label='Actual price', color='blue', marker = 'o')
#plt.plot(range(0,len(result[700:800])), pred_y[700:800], label='Predicted price', color='red', marker ='x')
#plt.xlabel('Hours')
#plt.ylabel('Price ($)')
#plt.title('Bitcoin Price')
#plt.grid(True)
#plt.legend()
#plt.show()
print('回帰係数')
print(model.coef_)
print('切片 (誤差)')
print(model.intercept_)
print('決定係数')
print(model.score(X, Y))
