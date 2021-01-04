"""
設問1
故障状態のサーバアドレスとそのサーバの故障期間を出力
+
各サーバの過負荷状態となっている期間を出力するプログラム
(N回以上連続してタイムアウトした場合にのみ故障とみなす)
"""

#タイムアウト回数
N = 2
#直近の応答回数
m = 4
#応答時間
t = 50

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

print(IPv4_type[0])
print(Date_set[0])
print(ping_set[0])

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


#サーバ負荷判定
ping_load = [[] for i in range(len(IPv4_type))]
Date_load = [[] for i in range(len(IPv4_type))]

for j in range(len(IPv4_type)):
    for i in range(len(ping_set[j])):
        if ping_set[j][i] != '-':
            ping_load[j].append(ping_set[j][i])
            Date_load[j].append(Date_set[j][i])
    #整数化
    for i in range(len(ping_load[j])):
        ping_load[j][i] = int(ping_load[j][i])

    if m < len(ping_load[j]):
        test = sum(ping_load[j][-m:])/m
        if test > t:
            print("過負荷サーバ" + IPv4_type[j])
            print("期間" + Date_load[j][-m] + "〜" + Date_load[j][-1])

    else:
        test = sum(ping_load[j])/int(len(ping_load[j]))
        if test > t:
            print("過負荷サーバ" + IPv4_type[j])
            print("期間" + Date_load[j][0] + "〜" + Date_load[j][-1])
