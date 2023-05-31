import random


def ArrLst():
    list1 = []
    list2 = []
    for i in range(30):
        list1.append(random.randint(0, 10))
    list1.sort()
    print(list1)
    for i in list1:
        if i not in list2:
            list2.append(i)

    list2.sort()
    for i in list2:
        list1.remove(i)
    for i in list1:
        if i in list2:
            list2.remove(i)
    print(list2)

ArrLst()