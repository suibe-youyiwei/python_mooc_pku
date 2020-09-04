#将n转换为base进制数
def toStr(n,base):
    convertString = '0123456789ABCDEF'
    if n<base:
        return convertString[n]     #最小规模
    else:
        return toStr(n//base,base)+convertString[n%base]   #减小规模，调用自身

print(toStr(1000,2))