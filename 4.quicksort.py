# divide and conquer

# 1. Figure out a simple case as best case
# 2. Figure out how to reduce problem to get to the base case

# solve recursively

# base case is array of 0 or 1

# sum(246) = 12 is the same as 2 + sum(46) = 2 + 10 = 12

def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

print(sum([1,2,3,4]))

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print(count([1,2,3,4]))

def max_number(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(max_number([1,2,7,4]))

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        
        less = [i for i in array[1:] if i <= pivot] # sub-array of all elements less than pivot

        greater = [i for i in array[1:] if i >= pivot] # sub-array of all elements greater than the pivot

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([5,8,1,5,3,1,2,8,9,6,4,7,5,8,9,2,5,4,6,47891641,4,8,5,3,6,2,1,4]))