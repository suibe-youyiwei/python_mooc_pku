#Stack类用于实现栈以及栈的基本功能
#以列表最后一个元素作为栈顶
#包括：
#isEmpty() 用于判断栈是否为空
#push() 用于向栈中添加数据项
#pop() 用于取出栈中的数据项
#peek() 用于窥探栈顶的数据项
#size() 用于知道栈的大小
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


