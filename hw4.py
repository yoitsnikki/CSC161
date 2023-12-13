'''
Niharika Agrawal
CSC 161
HW 4
'''

def main():
    q = input("Please enter the file name of the financial data: ")

    #open file, extract data into list, and close file
    fd = open(q, 'r')

    data = []

    for line in fd:
        for word in line.split():
            data.append(word)
    fd.close()

    data.insert(6, 1000.0)

    #assign variables
    p = float(data[1])
    i = format(float(data[3]), ".1%")
    y = float(data[5])

    #print beginning data
    print("\nThe initial principle is: " + str(p))
    print("Annual Percentage Rate is: " + str(i))
    print("Length of Term: " + str(int(y)))

    #print year values
    print("\nYear Value")

    for a in range(11):
        print("{:4}".format(str(a) + " " + str("${:.2f}".format(float(data[a+6])))))
    
main()
