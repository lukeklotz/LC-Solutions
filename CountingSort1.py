def countingSort(arr):
    # Write your code here
    counter = {}
    
    for num in arr:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    
    res = []
    for i in range(len(arr)):
        if i in counter:
            res.append(counter[arr[i]])
        else:
            res.append(0)
        
    return res

arr = [1,1,3,2,1,4,2,5,2,2,2,1,2,0]

print(countingSort(arr))
