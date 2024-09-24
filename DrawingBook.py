def pageCount(n, p):
    # Write your code here
    count = 0
    l = 0
    r = 1
    curr_page = [l, r]
    
    #start from back
    if p > n//2:
        l = n - 1
        r = n 
        curr_page[0] = l
        curr_page[1] = r
        while l >= p and r >= p:
            l -= 2
            r -= 2
            curr_page[0] = l
            curr_page[1] = r
            count += 1
    #start from front
    else:
        while l <= p and r <= p:
            l += 2
            r += 2
            curr_page[0] = l
            curr_page[1] = r
            count +=1
    
    return count
    

    #not the correct solution but wanted to post my attempt
    # gonna try again tomorrow!