import pybitflyer
import pandas as pd
from datetime import datetime
api = pybitflyer.API(api_key="",api_secret="") #ここにapiキーを入力
tick = api.ticker(product_code="FX_BTC_JPY")#FX_BTC_JPYかBTC_JPYを選択
time = datetime.now().strftime("%Y/%m/%d %H:%M:%S") #apiにも時刻あるけど、扱いやすいのでこっちにする
ask = tick["best_ask"]
bid = tick["best_bid"]
mid = ( ask + bid ) / 2 #ASKとBIDの中間値をとる
df = pd.read_csv('./sma.csv') #価格、SMAデータを読み込む。
df2 = pd.read_csv('./sma_profit.csv') #利益データを読み込む。
sma15=0
sma50=0
for j in range(1,16):
    try:
        sma15+=df.iloc[-j,1]
    except IndexError:
        pass
for k in range(1,51):
    try:
        sma50+=df.iloc[-k,1]
    except IndexError:
        pass
row = pd.Series([time,mid,sma15/15,sma50/50], index=df.columns) #行つくる
df = df.append(row,ignore_index=True) #行たす
df.to_csv('./sma.csv',index=None) #かく
positions=api.getpositions(product_code="FX_BTC_JPY")#FX_BTC_JPYかBTC_JPYを選択
change = api.getcollateralhistory()
profit = change[0]['change']
amount = change[0]['amount']
print("good")
sum = 0
try:
    if df.iloc[-2,2] <= df.iloc[-2,3] and df.iloc[-1,2] >= df.iloc[-1,3]:
        api.sendparentorder(order_method="IFDOCO",
                           parameters=[{
                               "product_code": "FX_BTC_JPY",
                               "condition_type": "MARKET",
                               "side": "BUY",
                               "size": 0.01
                           },
                               {
                                   "product_code": "FX_BTC_JPY",
                                   "condition_type": "TRAIL",
                                   "side": "SELL",
                                   "offset": 2000,
                                   "size": 0.01
                               },
                               {
                                   "product_code": "FX_BTC_JPY",
                                   "condition_type": "STOP",
                                   "side": "SELL",
                                   "trigger_price": int(mid) - 1500,
                                   "size": 0.01
                               }]
                           )
        print("buy")
        position = 'long'
        row2 = pd.Series([time,amount,position], index=df2.columns) #行つくる
        df2 = df2.append(row2,ignore_index=True) #行たす
        df2.to_csv('./sma_profit.csv',index=None) #かく
    if df.iloc[-2,2] >= df.iloc[-2,3] and df.iloc[-1,2] <= df.iloc[-1,3]:
        api.sendparentorder(order_method="IFDOCO",
                            parameters=[{
                                "product_code": "FX_BTC_JPY",
                                "condition_type": "MARKET",
                                "side": "SELL",
                                "size": 0.01
                            },
                                {
                                    "product_code": "FX_BTC_JPY",
                                    "condition_type": "TRAIL",
                                    "side": "BUY",
                                    "offset": 2000,
                                    "size": 0.01
                                },
                                {
                                    "product_code": "FX_BTC_JPY",
                                    "condition_type": "STOP",
                                    "side": "BUY",
                                    "trigger_price": int(mid) + 1500,
                                    "size": 0.01
                                }]
                            )
        print ("sell")
        position = 'short'
        row2 = pd.Series([time,amount,position], index=df2.columns) #行つ>くる
        df2 = df2.append(row2,ignore_index=True) #行たす
        df2.to_csv('./sma_profit.csv',index=None) #かく
except IndexError:
    pass
