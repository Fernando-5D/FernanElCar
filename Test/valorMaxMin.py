def valorMax(*args):
    max = 0
    for x in args:
        if max < x:
            max = x
    
    return max

def valorMin(*args):
    min = 0
    for x in args:
        if min > x:
            min = x
    
    return min

nums = [5, 6, 3, 9, 1, 7, 2, 8, 4]
print(str(valorMax(nums)))
print(str(valorMin(nums)))