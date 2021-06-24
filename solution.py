import operator
a = []
l = [[input(), float(input())] for _ in range(int(input()))]
#print(l)
k = sorted(l, key=lambda x: x[1])
#print(k)
g = k[0]
h = k[1]
o = []
if g[1] != h[1]:
    g = k[2]
    if h[1] != g[1]:
        print(h[0])
    else:
        o.append(g)
        o.append(h)
        sorted_list = sorted(o, key=operator.itemgetter(0))
        for i in sorted_list:
            print(i[0])

elif g[1] == h[1]:
    g = k[2]
    h = k[3]
    if g[1] != h[1]:
        print(h[0])
    else:
        o.append(g)
        o.append(h)
        sorted_list = sorted(o, key=operator.itemgetter(0))
        for i in sorted_list:
            print(i[0])
else:
    if g[1] == h[1]:
        g = k[2]
        if h[1] == g[1]:
            h = k[3]
            if g[1] != h[1]:
                print(h[0])
