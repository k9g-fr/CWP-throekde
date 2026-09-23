mylist = []
start = input()
stop = input()
if not start or not stop:
    print("none")
else:      
    for i in range(int(start), int(stop)+1):
        mylist.append(i)
    print(mylist)
