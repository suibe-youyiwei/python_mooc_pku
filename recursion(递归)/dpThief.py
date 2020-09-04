tr = [None,{'w':2,'v':3},{'w':3,'v':4},{'w':4,'v':8},{'w':5,'v':8},{'w':9,'v':10}]
max_w = 20
m = {(i,w):0 for i in range(len(tr)) for w in range(max_w+1)}

for i in range(1,len(tr)):
    for w in range(1,max_w+1):
        #如果第i个宝物重量太大,无法带走,则m(i,w) = m(i-1,w)
        if tr[i]['w']>w:
            m[(i,w)] = m[(i-1,w)]
        #或者第i个宝物重量适中,则取带走或者不带走中的最大值,其中带走时m(i,w) = vi + m(i-1,w-wi)
        else:
            m[(i,w)] = max(m[(i-1,w)],m[(i-1,w-tr[i]['w'])]+tr[i]['v'])
print(m[(len(tr)-1,max_w)])