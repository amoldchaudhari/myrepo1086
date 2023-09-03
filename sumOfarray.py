# Write a Python function that takes an array of integers as input and returns the sum of all the elements in the array. Optimize the function for large arrays.

num = [2,5,8,8]
def simpleArraySum(ar):
    intiger = 0
    for index in ar:
        intiger = intiger + index
    print(intiger)
    return intiger
simpleArraySum(num)