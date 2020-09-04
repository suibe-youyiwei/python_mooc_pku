#使用链表实现有序表
from LinkList import Node,LinkList

class OrderedList():
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        stop = False
        found = False
        while not found and not stop and current!=None:
            if current.getData() == item:
                found = True
            else:
                if current.getData()>item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self,item):
        current = self.head
        pre = None
        temp = Node(item)
        while current != None:
            if current.getData() > item:
                break
            else:
                pre = current
                current = current.getNext()
        if pre == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            pre.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 1
        current = self.head
        while current.next!=None:
            count+=1
            current = current.getNext()
        return count

    def index(self,item):
        index = 0
        current = self.head
        while current!=None:
            if current.getData() == item:
                return index
            else:
                current = current.getNext()
                index+=1
        return "Could not find the item"

    def pop(self, pos=-1):
        index = 0
        current = self.head
        pre = None
        while current.next != None:
            pre = current
            current = current.getNext()
            index += 1
            if index == pos:
                val = current.getData()
                pre.setNext(current.getNext())
                return val
        if pos == -1:
            val = current.getData()
            pre.setNext(None)
            return val
        else:
            return "Could not find the position"

    def remove(self,item):
        current = self.head
        pre = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                pre = current
                current = current.getNext()
        if pre == None:  # 即item为表头
            self.head = current.getNext()
        else:
            pre.setNext(current.getNext())


ol = OrderedList()
print(ol.isEmpty())
ol.add(1)
ol.add(2)
ol.add(3)
ol.add(4)
print(ol.size())
print(ol.index(1))
print(ol.index(4))
print(ol.search(3))
print(ol.pop(1))
print(ol.search(2))