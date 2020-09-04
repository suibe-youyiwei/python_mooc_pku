#deque用于定义双端队列
#使用list的首端作为双端队列的首端，尾端作为双端队列的尾端
class Deque():
    #创建空的双端队列
    def __init__(self):
        self.items = []

    #将item加入队首和队尾
    def addFront(self,item):
        self.items.insert(0,item)

    def addRear(self,item):
        self.items.append(item)

    #将尾端或者首端的数据项移除
    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    #返回是否为空
    def isEmpty(self):
        return self.items == []

    #返回大小
    def size(self):
        return len(self.items)