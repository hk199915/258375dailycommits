tup = (1, 2, 3, 4, 4, 5, 5, 12, 12, 12, 12, 1, 3, 2, 4, "my", "my", "hi", "hi", "hello")
rep = []
for i in tup:
    if tup.count(i) > 1:
        rep.append(i)
    else:
        continue
for x in rep:
    while rep.count(x) > 1:
        rep.remove(x)

print("Repeated items:", tuple(rep))