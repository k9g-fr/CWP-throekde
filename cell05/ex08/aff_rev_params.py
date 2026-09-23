t1 = input()
t2 = input()
t3 = input()
x = []
if not t1 or not t2 or not t3:
    print("none")
else:
    x.append(t3)
    x.append(t2)
    x.append(t1)
    for i in x:
        print(i)