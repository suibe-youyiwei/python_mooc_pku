#定义链表节点
#另一种链表定义方法见图解算法（LeetCode题目）链表

class Node:
    def __init__(self,val):
        self.next = None
        self.data = val

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newval):
        self.data = newval

    def setNext(self,newnext):
        self.next = newnext

class LinkList():
    def __init__(self):
        self.head = None #定义表头指向的下一个节点为None
