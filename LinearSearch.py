def linear_search(arr, target):
    #loop though items in array
    for id in range(len(arr)):
        #check if item at current index equals target
        if arr[id] == target:
            #return current index as the match
            return id
    #if we get here means no match found
    return -1


