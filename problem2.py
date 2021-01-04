"""
設問1
故障状態のサーバアドレスとそのサーバの故障期間を出力するプログラム
(N回以上連続してタイムアウトした場合にのみ故障とみなす)
"""

#タイムアウト回数
N = 1

#ログファイルからデータを取得
f = open('log.txt', 'r')
datalist = f.readlines()
f.close()

#ログファイルの行数
M = len(datalist)

Date = []
IPv4 = []
ping = []

for i in range(M):
    a = datalist[i].split(',')
    #ログデータを分割
    Date.append(a[0])
    IPv4.append(a[1])
    ping.append(a[2].rstrip('\n'))  #改行取り除き

#サーバごとの情報に分ける
IPv4_type = list(dict.fromkeys(IPv4))#サーバの種類

Date_set = [[] for i in range(len(IPv4_type))]
ping_set = [[] for i in range(len(IPv4_type))]

for i in range(len(IPv4_type)):
    for j in range(M):
        if IPv4[j] == IPv4_type[i]:
            Date_set[i].append(Date[j])
            ping_set[i].append(ping[j])

#サーバごとに故障判定
#タイムアウト回数判定
for k in range(len(IPv4_type)):
    for i in range(len(ping_set[k])):
        if ping_set[k][i] == '-':
            if ping_set[k][i+1] == '-' and ping_set[k][i-1] != '-':
                for j in range(len(ping_set[k])-i-1):
                    if ping_set[k][i+1+j] != '-' and j >= N:
                        print("故障サーバ" + IPv4_type[k])
                        print("故障期間" + Date_set[k][i] + "〜" + Date_set[k][i+1+j])
                        break

            elif N==1 and ping_set[k][i+1] != '-' and ping_set[k][i-1] != '-':
                print("故障サーバ" + IPv4_type[k])
                print("故障期間" + Date_set[k][i] + "〜" + Date_set[k][i+1])
