import itertools
s = itertools.product("ГЕПАРД", repeat=5)
a = []
l = []
cnt = 0
for i in s:
    a.append(list(i))
for e in a:
    if e.count("Г") == 1 and e[0] != "А" and e[-1] != "Е":
        l.append(e)
        cnt += 1
print(cnt)