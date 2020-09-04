#贪心算法找零问题
class greedy():
    def __init__(self):
        self.coin = [20,10,5,1]
        self.res = []

    def charge(self,money):
        coins = self.coin
        res = self.res
        def divide(left,i,coins):
            coin = coins[i]
            num = left//coin
            res.append(num)
            left_next = left%coin
            if left_next>0:
                i+=1
                divide(left_next,i,coins)
        divide(money,0,coins)
        return res
g = greedy()
print(g.charge(122))


