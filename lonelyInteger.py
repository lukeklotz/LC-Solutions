def lonelyinteger(a):
    # initialize dictionary
    counter = {}

    for num in a:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    
    for num in a:
        print(f"this is num:  {num}")
        print(f"this is counter[num]:  {counter[num]}")
        print(" ")
        if counter[num] == 1:
            return num

a = [1,1,2,2,3,3,4,4,5,5,6]

lonelyinteger(a)


#modified this so I could see what was going on with the dictionary
#still learning how dictionaries work but after this I think I get it

#the first for loop utilizes a dictionary to count the number of occurrances
#for each number in the list

#the second for loop checks which of the numbers has a count of 1 and then returns
#whatever number that was

# num == number in the list
# counter[num] == the Amount Of That Number     
