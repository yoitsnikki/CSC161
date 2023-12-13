'''
Niharika Agrawal
CSC 161
HW 5
'''

#turn all list items into numbers after being read
def to_numbers(str_list):

    length = len(str_list)

    for i in range(length):
        str_list[i] = int(str_list[i])

    return str_list

#function to square all values of a list and replace the values
def square_each(nums):

    length = len(nums)

    for i in range(length):
        nums[i] = nums[i]**2

#function to sum all numbers in a list
def sum_list(nums):

    length = len(nums)
    sumList = 0

    for i in range(length):
        sumList = sumList + nums[i]

    return sumList

#main function that calls all three previous functions with a read file
def main():

    #read data file
    q = input("Please enter the file name: ")
    fd = open(q, 'r')

    str_list = fd.readlines()
    fd.close()

    #run functions
    nums = to_numbers(str_list)
    square_each(nums)
    finalSum = sum_list(nums)

    print("The sum of the squares of the numbers in the file is " + str(finalSum))

main()
