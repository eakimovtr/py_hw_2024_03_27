def sort(arr: list) -> list:
    avg: float = sum(arr) / len(arr)
    if avg > 0:
        boundary = len(arr) * 2 // 3
    else:
        boundary = len(arr) // 3
    return sorted(arr[:boundary]) + [n for n in reversed(arr[boundary:])]
    
    
arr = [-9,-1,-8,-2,-7,-3,6,4,5]
print(sort(arr))

arr = [9,1,8,2,7,3,6,4,5]
print(sort(arr))