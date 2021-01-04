# プログラミング試験
このリポジトリは株式会社フィックスポイント様のプログラミング試験について，解答をまとめたものである．
以下に設問1〜4のそれぞれについて，作成したプログラムの解説および実行結果を示す．
言語はPythonを用いた．

## 設問1
監視ログファイルを読み込み，故障状態のサーバアドレスとそのサーバの故障期間を出力するプログラムである．
なお，pingがタイムアウトした場合を故障とみなし、最初にタイムアウトしたときから、次にpingの応答が返るまでを故障期間とする．
プログラムのファイル名はproblem1.pyである．

### 解説
まず初めに監視ログファイルlog.txtを読み込む．
監視ログは１行ごとに
＜確認日時＞,＜サーバアドレス＞,＜応答結果＞
のようにカンマ区切りの形式で並んでいるので，各行についてカンマごとに分割し，
サーバごとに確認日時，応答結果の情報をそれぞれ配列Date[i], ping[i]にまとめる．

この後，各サーバに対して，故障状態かどうかを判定する．
タイムアウトしている場合，応答結果は"-"(ハイフン記号)と表示されるので，
次の手順で故障状態の判定を行う．
- 応答時間ping[i]が"-"の場合，
  - 1つ前の応答時間ping[i-1]が"-"でない，かつ1つ後の応答時間ping[i+1]が"-"である場合，
    - 2つ後以降の応答時間ping[i+1+j]が"-"でなくなる場合， 
    故障期間はDate[i]からDate[i+1+j]となる．
  - 一つ前の応答時間ping[i-1]が"-"でない，かつ一つ後の応答時間ping[i+1]が"-"でない場合，  
  故障期間はDate[i]からDate[i+1]となる．
- 応答時間に"-"がない場合，  
故障期間なし．

### 実行結果
hoge

## 設問2
設問1で作成したプログラムを拡張する．
設問1では全てのタイムアウトを故障とみなしていたが，
設問2では*N*回以上連続してタイムアウトした場合にのみ故障とみなすプログラムとなっている．
プログラムのファイル名はproblem2.pyである．

### 解説
故障状態の判定方法を次のように変更すればよい．
- 応答時間ping[i]が"-"の場合，
  - 1つ前の応答時間ping[i-1]が"-"でない，かつ1つ後の応答時間ping[i+1]が"-"である場合，
    - 2つ後以降の応答時間ping[i+1+j]が"-"でない，**かつj+1がNより大きい場合**,  
    故障期間はDate[i]からDate[i+1+j]となる．
  - **N=1で与えられている**，かつ一つ前の応答時間ping[i-1]が"-"でない，かつ一つ後の応答時間ping[i+1]が"-"でない場合，  
  故障期間はDate[i]からDate[i+1]となる．
- 応答時間に"-"がない場合，  
故障期間なし．

太字が変更箇所である．

### 実行結果
hoge

## 設問3
設問2で作成したプログラムを拡張する．
各サーバの過負荷状態を判定し，過負荷状態になっている期間を出力するプログラムを作成する．
ここで過負荷状態とは，直近*m*回の平均応答時間が*t*ミリ秒を超えた場合のことを指す．
プログラムのファイル名はproblem3.pyである．

### 解説
まず各サーバに対して，応答結果ping[i]からタイムアウト"-"の要素を取り除く．
するとping[i]には数字の文字列の要素のみ残るので，それらを全て整数化する．
こうしてできる配列を改めてping_load[i]とする

このあと次のように過負荷状態を判定する．
- ping_load[i]の要素数がmより大きい場合，
  - ping_load[i]の後ろm個の要素を取り出しそれらを足し合わせmで割る．その数がtより大きい場合  
  そのサーバは過負荷状態であり，過負荷期間はDate[-m]からDate[-1]
  - そうでない場合
  過負荷期間なし
- ping_load[i]の要素数がmより小さい場合，
  - ping_load[i]の全要素を足し合わせ要素数で割る．その数がtより大きい場合
  そのサーバは過負荷状態であり，過負荷期間はDate[0]からDate[-1]
  - そうでない場合  
  過負荷期間なし

### 実行結果
hoge

## 設問4
設問3で作成したプログラムを拡張する．
各サブネット毎にネットワークの故障期間を出力できるようなプログラムを作成する．
ネットワーク経路にあるスイッチに障害が発生した場合、そのスイッチの配下にあるサーバの応答がすべてタイムアウトすると想定される。
そこで、あるサブネット内のサーバが全て故障（ping応答がすべて*N*回以上連続でタイムアウト）している場合は、
そのサブネットの故障とみなす．
プログラムのファイル名はproblem4.pyである．

### 解説
サーバ0とサーバ1が同じサブネットにあるとする．
最初にping[0][i]とping[1][i]の2つの配列
(1つ目のインデックスはサーバの種類を表す)で，
どちらも要素が"-"になっている箇所を探す．
どちらも要素が"-"の場合True，そうでない場合Falseとなる配列を新たに考えれば，
設問2と同じ方法でサブネットの故障判定を行うことができる．

### 実行結果
hoge
