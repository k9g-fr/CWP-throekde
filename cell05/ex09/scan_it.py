word = input()
sentence = input()
if not word or not sentence:
    print("none")
else:
    x = sentence.split()
    count = x.count(word)
    print(count)