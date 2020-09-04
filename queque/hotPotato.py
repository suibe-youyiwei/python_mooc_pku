from queue import Queue

#这个程序用于使用队列模拟传土豆的游戏
#传土豆的游戏类似于击鼓传花，确定传递次数，传到的人被淘汰
#nameList为玩游戏的人员名单列表，num为土豆传递次数
def hotPotato(nameList,num):
    simqueue = Queue()
    for name in nameList:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue()) #进行一次传递
        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["A","B","C","D","E","F"],7))