from stack import Stack
#这是一个用于将中缀表达式转换为后缀表达式的函数
#传入infix为中缀表达式字符串
def infixToPostfix(infix):
    tokenList = []
    for i in infix:
        tokenList.append(i)
    opStack = Stack()
    postfixList = []
    #定义运算符优先级
    pre = {}
    pre["/"] = 3
    pre["*"] = 3
    pre["+"] = 2
    pre["-"] = 2
    pre["("] = 1

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken!="(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (pre[token]<=pre[opStack.peek()]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    postfix = "".join(postfixList)
    return postfix

print(infixToPostfix("(A+B*C)*D+E"))

"""
算法详解：
中缀表达式转换为后缀表达式算法为：将表达式每一个最小元素作为一个token，对于每一个token，如果token为运算数
则将token输出，放入postfixList。如果token为"("，则将token push到opStack(栈)中。如果token为")"，则考虑opStack
中栈顶的topToken是否为")"，如果不是,则输出topToken。如果token为运算符，则考虑token和opStack中栈顶的topToken的优先级，
如果token优先级高，则将token push入opStack；如果topToken优先级高，则将topToken输出，知道opStack为空或者token优先级高。
最后使用join输出后缀表达式的字符串
"""


#这是一个用于计算后缀表达式的函数
def postfixEval(postfix):
    opStack = Stack()
    tokenList = []
    for i in postfix:
        tokenList.append(i)
    for token in tokenList:
        if token in "0123456789":
            opStack.push(int(token))
        else:
            right_num = opStack.pop()
            left_num = opStack.pop()
            opStack.push(doMath(left_num,right_num,token))
    return opStack.pop()

def doMath(l_num,r_num,token):
    if token == "*":
        return l_num*r_num
    elif token == "/":
        return l_num/r_num
    elif token == "+":
        return l_num+r_num
    else:
        return l_num-r_num

postfix = infixToPostfix("(1+2*3)+4")
print(postfix)
print(postfixEval(postfix))

"""
对于后缀表达式求值的算法为：如果token为操作数，则将其push入opStack。如果token为操作符，则将opStack中最上面的两个
操作数pop出来，进行求值，再push入opStack。最终opStack中所剩的唯一操作数即为求值。
"""