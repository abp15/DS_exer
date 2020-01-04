def ins_sort(a):
    for i in range(1,len(a)):
        for j in range(i-1,-1,-1):
            if a[j] > a [j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            else:
                break
    return a


def ins_sort2(a):
    for i in range(1,len(a)):
        j = i-1
        while a[j] > a [j+1] and j >=0:
                a[j], a[j+1] = a[j+1], a[j]
    return a



def ins_sort3(a):
    for i in range(1,len(a)):
        curNum = a[i]
        for j in range(i-1,0,-1):
            if a[j] > curNum:
                a[j+1] = a[j]
            else:
                j+=1
                break
            a[j]=curNum
    return a



def sel_sort(a):
    for i in range(0,len(a)-1):
        minIndex = i
        for j in range(i+1,len(a)):
            if a[j] < a [minIndex]:
                minIndex = j
            if minIndex != i:
                a[j], a[minIndex] = a[minIndex], a[j]

    return a

def bub_sort(a):
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-1-i):
            if a[j] > a [j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a
    
