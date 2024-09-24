def diagonalDifference(arr):
    totRight = 0
    totLeft = 0
    
    rCounter = len(arr[0]) - 1
    lCounter = 0
    
    for i in range(len(arr)):
        totRight += arr[i][rCounter]
        totLeft += arr[i][lCounter]
        
        rCounter -= 1
        lCounter += 1
        
    return abs(totRight - totLeft)


#I overthought this on my first attempt and used a very complicated nested for loop 
#not even sure how I got the first one working..

#but I refreshed my braid and looked at it again today and found this much simpler
#approach pretty quick, so that felt good!

#since we're always dealing with a square 2D array, we only have to iterate through
#the ROWS of the array. We set up two pointer (rCounter and lCounter). 
#lCounter = 0 and rCounter = len(arr[0]) - 1

#on each iteration of the loop, we can add the values that out pointers are pointing to
#and then increment the left, and decrement the right.

