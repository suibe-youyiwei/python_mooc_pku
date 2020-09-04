#minCoins为列表对象，存储每块钱的最优找零结果
def dpMakeChange(coinList,change,minCoins):
    for cents in range(1,change+1):
        coinCount = cents
        for j in [c for c in coinList if c<=cents]:
            if minCoins[cents - j]+1<coinCount: #减去每种硬币，向后查找最少的找零结果
                coinCount = minCoins[cents - j]+1
        minCoins[cents] = coinCount #记录每块钱的最优找零结果
    return minCoins[change] #返回最后一个结果，即为最终结果

print(dpMakeChange([1,5,10,25],63,[0]*64))

#dpMakeChange_2可以返回所有的最优解发的使用硬币
def dpMakeChange_2(coinList,change,minCoins,coinUsed):
    for cents in range(1,change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinList if c<=cents]:
            if minCoins[cents - j]+1<coinCount:
                newCoin = j
                coinCount = minCoins[cents - j]+1
        minCoins[cents] = coinCount
        coinUsed[cents] = newCoin
    return minCoins[change],coinUsed

def printCoin(coinUsed,change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin
coinUsed = [0]*64
dpMakeChange_2([1,5,10,21,25],63,[0]*64,coinUsed)
printCoin(coinUsed,63)
print(coinUsed)