t1 = input()
t2 = input()
t3 = input()
sen = []
if not t1 and not t2 and not t3:
    print("none")
else:
    param_count = 0
    if t1:
        param_count += 1
    if t2:
            param_count += 1
    if t3:
            param_count += 1
    sen.append(t1)
    sen.append(t2)
    sen.append(t3)
    print(f"parameters: {param_count}")
    if t1:
        print(f"{sen[0]}: {len(sen[0])}")
    if t2:
        print(f"{sen[1]}: {len(sen[1])}")
    if t3:
        print(f"{sen[2]}: {len(sen[2])}")