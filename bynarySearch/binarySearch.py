import math

def binarySearch(arr, target)
  left = 0 
  right = len(arr) -1
  
  while(left <= right):
    mid = math.floor(left + (right - left ) / 2)
    
    if arr[mid] == target:
      return mid
    
    iff arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
    return -1

arr = [1,2,3,4,5,6]
target = 6

result = binarySearch(arr, target)

if result != -1:
  print("Element is present at index %d"%result)
else:
  print("Element is not present in array")
  
  
