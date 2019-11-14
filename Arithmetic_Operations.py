"""Python program to perform arithemetical operation"""
import os
def addition(VAL_ONE, VAL_TWO):
    """ Addition function to find sum of 2 numbers"""
    result = VAL_ONE + VAL_TWO
    return result

def subtraction(VAL_ONE, VAL_TWO):
    """Subtraction function to find the difference of 2 numbers"""
    result = VAL_ONE - VAL_TWO
    return result

def multiplication(VAL_ONE, VAL_TWO):
    """multiplication function find the product of 2 numbers"""
    result = VAL_ONE * VAL_TWO
    return result

def division(VAL_ONE, VAL_TWO):
    """Divison function find the quotient of 2 nubers"""
    result = VAL_ONE / VAL_TWO
    return result

if __name__ == '__main__':

    print "MENU ...\n 1)Addition\n 2)Subtraction\n 3)Muliplication\n 4)Divison"
    OPTION = int(raw_input("Please choose an arithmetic operation from the above menu\t"))

    if OPTION == 1 or OPTION == 2 or OPTION == 3 or OPTION == 4:
        INPUT1 = int(raw_input("Please enter the first number\t"))
        INPUT2 = int(raw_input("Please enter the second number\t"))
    else:
        print "Invalid option"

    if OPTION == 1:
        print addition(INPUT1, INPUT2)

    elif OPTION == 2:
        print subtraction(INPUT1, INPUT2)

    elif OPTION == 3:
        print multiplication(INPUT1, INPUT2)

    elif OPTION == 4:
        print division(INPUT1, INPUT2)
    else:
        pass

    os.system("pause")
