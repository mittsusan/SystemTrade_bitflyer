# SystemTrade for bitflyer

## 概要
bitflyerでシステムトレードをするためのプログラムです。python(pybitflyer)を元に作らせていただいています。  
pythonの基礎知識はある程度必要です。
## 注意事項
プログラムを使用する際はお金が直接関わるので**自己責任**で行なってください。  
また、このプログラムでは取引額が0.01BTCに設定されているのでそこは各自で修正して使って下さい。
最初にプログラムを使用し始めると、前のデータが参照されるので最初の注文だけは上手くいかない場合がありますので、そこはご了承下さい。（要望がありましたら、修正致します。）
## 使用方法

### 1分間隔のSMA15,SMA50を使ったプログラムでの例
まず、最初に  
```git@github.com:mittsusan/systemtrade_pybitflyer.git ```  
をして、ファイルを入手してください。  

そして  
```pip install pybitflyer```  
をして、pybitflyerをインストールして下さい。
次に、下準備でsma.pyの中の  

```sma.py
api = pybitflyer.API(api_key="",api_secret="") #ここにapiキーを入力
```  
の行にAPIキーを入力して下さい。  
  APIキーについては[こちら](http://neoshanaineet.com/virtual-currency/bitflyer-lightning-get-apikey.html)を参照して下さい。 
  
  次に  
  
```sma.py
df = pd.read_csv('./sma.csv') #価格、SMAデータを読み込む。
df2 = pd.read_csv('./sma_profit.csv') #利益データを読み込む。
df.to_csv('./sma.csv',index=None) #かく
df2.to_csv('./sma_profit.csv',index=None) #かく
df2.to_csv('./sma_profit.csv',index=None) #かく
```  
この./の部分を絶対パスに書き換えて下さい。  
また、sma.txtの

```sma.txt
* * * * * /usr/local/bin/python3 ./sma.py >>./exec.log 2>>./exec_error.log
```
この./の部分も絶対パスに書き換えて下さい。

      
  
  そして、sma.txt内の```/usr/local/bin/python3```  の部分は人それぞれ、pythonのインストールした場所のパスを通して下さい。 
  
  最後に  
```crontab　sma.txt```  
を行えば、1分間隔でプログラムが動き出します。止めたい時は  
```crontab -r```  
で止まります。  

## 参照  
http://wolfin.hatenablog.com/entry/2016/08/29/010112  

## 最後に  
色々な人に使って頂きたく、作らさせて頂きました。ご質問、ご要望などはぜひ承りますので、何卒よろしくお願い致します。

