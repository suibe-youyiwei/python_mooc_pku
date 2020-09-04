#queue用于定义队列
#包括创建队列，插入元素，弹出元素，判断是否为空，判断大小等功能
#使用python的list容纳数据项，且将list的首端作为queue的尾端，list的末端作为queue的首端

class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return (self.items == [])