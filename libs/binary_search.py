def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None

def bs_left(list, target):
    low = 0
    high = len(list)

    while low < high:
        mid = (low + high) // 2
        if target > list[mid]:
            low = mid + 1
        else:
            high = mid
    return low

def bs_right(list, target):
    low = 0
    high = len(list)
    while low < high:
        mid = (low + high) // 2
        if target < list[mid]:
            high = mid
        else:
            low = mid + 1
    return low


