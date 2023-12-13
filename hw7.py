'''
Niharika Agrawal
CSC 161
HW 7
'''

def get_input():
    l0 = 0
    while l0 != 1:
        n = input("Enter the number of integers in the list: ")
        if str.isdigit(n) == True:
            l0 = l0 + 1
        else:
            print("Bad input!")

    nums = []

    l = 0
    while l != int(n):
        x = input("Enter an integer: ")

        if str.isdigit(x) == True:
            nums.append(x)
            l = l + 1

        else:
            print("Bad input!")

    l1 = 0
    while l1 != 1:
        k = input("Enter the target number: ")

        if str.isdigit(k) == True:
            l1 = l1 + 1
        else:
            print("Bad input!")

    return nums, k

def sum_to_k(nums, k):
    pairs = 0
    a = len(nums)

    for i in range(a):
        x1 = nums[i]
        m = i+1

        for j in range (a-(i+1)):
            x2 = nums[m]
            x3 = int(x1) + int(x2)
            m = m+1
            
            if x3 == int(k):
                pairs = pairs + 1

    return pairs
        
def main():
    nums, k = get_input()
    print(str(sum_to_k(nums, k)) + " pairs sum to " + str(k))

main()
