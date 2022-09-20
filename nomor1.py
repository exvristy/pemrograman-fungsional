def sum_square(x):
    if x == 1:
        return 1
    result = [i**2 for i in x]
    return sum(result)

list = [1,2,3]
print("Sum of element is ", sum_square(list))