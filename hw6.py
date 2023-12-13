'''
Niharika Agrawal
CSC 161
HW 6
'''

def is_valid(phone_number):
    
    n = [] #make a list

    #append all phone number characters to list
    for ch in phone_number:
        n.append(ch)

    rval = "False"

    #go through every digit in my list and check it
    while rval == "False":
        #is the length the exact length of phone numbers
        if len(n) != 12:
            break

        #digit by digit breakdown
        elif str.isdigit(n[0]) != True:
            break

        elif str.isdigit(n[1]) != True:
            break

        elif str.isdigit(n[2]) != True:
            break

        elif n[3] != "-":
            break

        elif str.isdigit(n[4]) != True:
            break

        elif str.isdigit(n[5]) != True:
            break

        elif str.isdigit(n[6]) != True:
            break

        elif n[7] != "-":
            break

        elif str.isdigit(n[8]) != True:
            break

        elif str.isdigit(n[9]) != True:
            break

        elif str.isdigit(n[10]) != True:
            break

        elif str.isdigit(n[11]) != True:
            break

        else:
            rval = "True"
            break

    if rval == "True":
        return True
    else:
        return False
              
def is_Rochester(phone_number):
    n = [] #make a list

    #append all phone number characters to list
    for ch in phone_number:
        n.append(ch)

    rval = "False"

    while rval == "False":
        if n[0] != "5":
            break

        elif n[1] != "8":
            break

        elif n[2] != "5":
            break

        else:
            rval = "True"

    if rval == "True":
        return True
    else:
        return False

def main():
    #get input
    phone_number = input("Please enter a phone number in format XXX-XXX-XXXX: ")
    v1 = is_valid(phone_number)
    v2 = False

    #print if phone number is valid
    if v1 == True:
        print(phone_number + " is valid")
        v2 = is_Rochester(phone_number)
    else:
        print(phone_number + " is not valid")

    #print if phone number is from Rochester
    if v2 == True:
        print(phone_number + " is from Rochester area")
        

main()
