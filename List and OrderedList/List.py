from LinkList import Node,LinkList
#使用链表定义无序表
class List():
    def __init__(self):
        self.head = None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head) #设置指向表头的下一个节点
        self.head = temp #设置表头

    def size(self):
        current = self.head
        count = 1
        while current!=None:
            current = current.getNext()
            count+=1
        return count

    def search(self,item):
        current = self.head
        while current!=None:
            if current.getData()==item:
                return True
                break
            else:
                current = current.getNext()
        return "Could not find the item"

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
        if pre == None: #即item为表头
            self.head = current.getNext()
        else:
            pre.setNext(current.getNext())

    def isEmpty(self):
        return self.head == None

    def append(self,item):
        current = self.head
        temp = Node(item)
        while current.next!=None:
            current = current.getNext()
        current.setNext(temp)

    def index(self,item):
        index = 0
        current = self.head
        while current!=None:
            if current.getData() == item:
                return index
            else:
                index+=1
                current = current.getNext()
        return "Could not find the item"

    def insert(self,pos,item):
        index = 0
        current = self.head
        pre = None
        temp = Node(item)
        if pos == index:
            self.add(item)
        else:
            while current!=None:
                index+=1
                pre = current
                current = current.getNext()
                if index == pos:
                    temp.setNext(current)
                    pre.setNext(temp)
                    return
            return "Could not insert into the LinkList"

    def pop(self,pos = -1):
        index = 0
        current = self.head
        pre = None
        while current.next!=None:
            pre = current
            current = current.getNext()
            index+=1
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

#test1
ls = List()
print(ls.isEmpty())
ls.add(1)
ls.add(2)
ls.add(4)
ls.insert(3,5)
ls.append(6)
print(ls.size())
print(ls.search(4))
ls.remove(4)
print(ls.search(4))
print(ls.pop())
print(ls.size())
print("------------------------------------")
#test2
ls = List()
ls.add(1)
ls.add(2)
ls.append(3)
ls.insert(1,4)
print(ls.index(1))
print(ls.index(2))
print(ls.index(3))
print(ls.index(4))