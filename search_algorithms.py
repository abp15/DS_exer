data = [5,6,7,8,9,10,11,12,17,21,25,27,35,37,42,45,50]
target = 12

## linear search

def linear_search(data, target):
    for i in range(len(data)-1):
        if data[i] == target:
            return i, True
    return False

## binary search iterative

def binary_search_iter(data, target):
    low = 0
    high= len(data)-1
    while low <=high:
        mid = (high+low)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid-1
        else:
            low = mid+1
    return False


## binary search recursive

def binary_search_recur(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recur(data,target, low, mid-1)
        else:
            return binary_search_recur(data,target, mid+1, high)
