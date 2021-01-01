import itertools

f = open("Input.txt", "r")
lines = f.readlines()

sum = 0
for l in lines:
    valueSet = set()
    toks = [x for x in l.split()]
    bad = False
    for t in toks:
        if t in valueSet:
            bad = True
            break
        valueSet.add(t)
    if not bad:
        sum = sum + 1
print("Part 1 Answer: " + str(sum))

sum = 0
for l in lines:
    valueList = []
    toks = [x for x in l.split()]
    ok = True
    for i in range(0, len(toks)):
        for j in range (i+1, len(toks)):
            iList = list(toks[i])
            jList = list(toks[j])
            if len(iList) == len(jList):
                for vi in iList:
                   if vi in jList:
                       jList.remove(vi)
                   else:
                       #something is different so it is ok
                       break
                if len(jList) == 0:
                    ok = False
            if not ok:
                break
        if not ok:
            break
    if ok:
        sum = sum + 1
print("Part 2 Answer: " + str(sum))
