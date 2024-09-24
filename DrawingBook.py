def pageCount(n, p):
    # Case 1: starting from the front
    front_flips = p // 2

    # Case 2: starting from the back
    if n % 2 == 0:
        back_flips = (n - p + 1) // 2
    else:
        back_flips = (n - p) // 2

    # Return the minimum of the two cases
    return min(front_flips, back_flips)
    

    #Passed most test cases with my original solution but not all
    #had to look up the solution

    #I like this approach because it doesnt involve a loop and therefor runs in O(1)
    #I might have been able to figure this out had I drawn out the problem on paper
    #From the very start I had a feeling there'd be a solution that didnt involve a loop
    #but I never tried to find it.. oh well! next time!