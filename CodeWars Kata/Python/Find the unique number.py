def find_uniq(arr):
    array = arr
    unique = set(array)
    dict = { number:0 for number in unique}
    for item in arr:
        dict[item] += 1
        
    for numbers in dict:
        if dict[numbers] == 1:
            return numbers
        else:
            pass
