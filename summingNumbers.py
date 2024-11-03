def summing(*args):
    sums = 0
    list_of_nums = [args]
    
    for element in list_of_nums:
        sums += element
    
    print(sums)


summing(10, 15, 75)
