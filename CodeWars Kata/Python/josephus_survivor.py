def josephus_survivor(n,k):
    copy = [x for x in range(1, n+1)]
    index = 0
    while len(copy) != 1:
        index += (k-1)
        if index >= len(copy):
            index %= (len(copy))
        copy.remove(copy[index])
        
        
    else:
        return copy[0]
