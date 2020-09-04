from stack import Stack
#这个程序用于实现简单括号匹配(只限“()”)
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index<len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index+=1

    if s.isEmpty() and balanced:
        return True
    else:
        return False

print(parChecker("((((()"))
print(parChecker("((()))"))


#用于复杂括号匹配
def complex_parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index<len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "[{(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not match(top,symbol):
                    balanced = False
        index+=1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def match(x,y):
    top = "({["
    symbol = ")}]"
    return top.index(x) == symbol.index(y)

s1 = "[{(())}]"
s2 = "[{{{{})((]"
print(complex_parChecker(s1))
print(complex_parChecker(s2))