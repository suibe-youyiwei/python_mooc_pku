from deque import Deque

def palchecker(string):
    checkdeque = Deque()
    for i in string:
        checkdeque.addRear(i)
    if checkdeque.size()%2 == 0:
        while checkdeque.size()>0:
            front = checkdeque.removeFront()
            rear = checkdeque.removeRear()
            if front!=rear:
                return False
        return True
    else:
        while checkdeque.size()>1:
            front = checkdeque.removeFront()
            rear = checkdeque.removeRear()
            if front!=rear:
                return False
        return True

print(palchecker('abbbba '))