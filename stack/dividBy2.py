from stack import Stack
#dividBy2()是用于将10进制数转换为2进制数的函数
def dividBy2(num_of_10):
    s = Stack()
    while num_of_10>0:
        rem = num_of_10%2
        s.push(rem)
        num_of_10 = num_of_10//2

    num_of_2 = ""
    while not s.isEmpty():
        num_of_2 = num_of_2+str(s.pop())
    return num_of_2

print(dividBy2(128))

#dividBy16用于转换10进制为16进制
def dividBy16(num_of_10):
    s = Stack()
    symbol = "ABCDEF"
    while num_of_10>0:
        rem = num_of_10%16
        if rem>=10:
            s.push(symbol[rem-10])
        else:
            s.push(rem)
        num_of_10 = num_of_10//16
    num_of_16 = ""
    while not s.isEmpty():
        num_of_16 = num_of_16+str(s.pop())
    return num_of_16

print(dividBy16(233))
