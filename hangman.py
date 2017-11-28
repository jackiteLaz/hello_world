from random import randint
dic = ["hello","world","banana"]
x = randint(0,2)
each = dic[x]
chosen = list(each)
rounds = 6
num = len(chosen)
points = 0
shown = []
while len(shown) != num:
    shown.append("#")
while points != len(shown) and rounds != 0:
    print(shown)
    print(chosen)
    let = input("enter a letter")
    for i in (0,len(chosen) - 1):
        if chosen[i] == shown[1]:
            points = points +1
    points = 0
    while let in chosen:
        for i in (0,len(shown)-1):
            if let == chosen[i]:
                del shown[i]
                shown.insert(i,chosen[i])              
print(shown)
print(chosen)
