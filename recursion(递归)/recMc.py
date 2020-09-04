def recMc(coinList,change):
    minCoins = change
    if change in coinList:
        return 1
    else:
        for i in [c for c in coinList if c<=change]:
            numCoins = 1+recMc(coinList,change - i)
            if numCoins<minCoins:
                minCoins = numCoins
    return minCoins
#print(recMc([1,5,10,25],66))

#将某一个change的最优解存储
def recDc(coinList,change,knownRes):
    minCoins = change

    if change in coinList:
        return 1
    elif knownRes[change]!=0:
        return knownRes[change] #直接查找最优解,可以大大提高递归效率
    else:
        for i in [c for c in coinList if c<=change]:
            numCoins = 1+recDc(coinList,change - i,knownRes)
            if numCoins<minCoins:
                minCoins = numCoins
    knownRes[change] = minCoins
    return minCoins
print(recDc([1,5,10,20],63,[0]*64))