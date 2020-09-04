#pythontest用于测试代码

#1 栈
from stack import Stack
s = Stack()
print(s.isEmpty())
s.push(4)
s.push('hello world')
s.push(True)
s.push(4.4)
print(s.size())
print(s.peek())
print(s.isEmpty())
print(s.pop())