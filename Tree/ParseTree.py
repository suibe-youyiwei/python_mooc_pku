from Tree.BinaryTree_2 import BinaryTree
from stack.stack import Stack

def buildParseTree(fpexp):
    fplist = []
    for i in fpexp:
        fplist.append(i) #分割为列表
    pStack = Stack() #新建栈用于保存父节点
    eTree = BinaryTree('') #创建树
    pStack.push(eTree) #当前节点入栈
    currentTree = eTree #设置当前节点
    for i in fplist:
        if i == "(": #当i为"("时 表达式开始 创建左子节点 当前节点下降 将老的当前节点（父节点）入栈
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ["+","-","*","/"] and i!=")": #当i为操作数时 节点值设置为操作数 上升
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ["+","-","*","/"]: #当i为操作符 当前节点值设置为操作符 下降到右子节点 并保存父节点入栈
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ")": #当i为")" 表达式结束 出栈上升到父节点
            currentTree = pStack.pop()
        else: #防止出错
            raise ValueError
    return eTree

import operator
def evaluate(parseTree):
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv} #存在问题
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

fpexp = "(3*(4+5))"
parseTree = buildParseTree(fpexp)
print(evaluate(parseTree))