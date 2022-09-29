########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


# import statements

# functions


def character_value(char):
    value = ord(char)
    value = value - 65
    return value


def get_school(user):
    if user == '1':
        print('School of Computing and Engineering SCE')
    elif user == '2':
        print('School of Law')
    elif user == '3':
        print('College of Arts and Sciences')
    else:
        print('Invalid School')


def get_grade(grade):
    if grade == '1':
        print('Freshmen')
    elif grade == '2':
        print('Sophomore')
    elif grade == '3':
        print('Junior')
    elif grade == '4':
        print('Senior')
    else:
        print('Invalid Grade')

sum1 = 0
def get_check_digit(card):
    if len(card) < 10:
        print("Must enter 10 chars")
    for index in range(len(card)):
        value = character_value(card[index])
        sum1 = (index + 1) * value
        check_digit: int = sum1 % 10
        return check_digit


def verify_check_digit(card):
    if len(card) < 10:
        print('The length of the number given must be 10')
    for i in range(0, 5):
        if (ord(card[i]) < 65) or (ord(card[i]) > 90):
            invalid = (card[i])
            return False, ",The first 5 characters must be A-Z, the invalid character is at" + str(i) + "is" + str(invalid)
    for i in range(7, 10):
        if (card[i] < 0) or (card[i] > 9):
            invalid = (card[i])
            return False, ",The last 3 characters must be 0-9, the invalid character is at" + str(i) + "is" + str(invalid)
    for i in range(6):
        if (card[5] != 1) or (card[5] != 2) or (card[5] != 3):
            return False, "The sixth character must be 1 2 or 3"
        else:
            pass
    for i in range(7):
        if card[6] != 1 or card[6] != 2 or card[6] != 3 or card[6] != 4:
            return False, "The seventh character must be 1 2 3 or 4"
        else:
            pass
    for i in range(10):
        if card[9] != get_check_digit(card):
            invalid = (card[9])
            i = (get_check_digit(card))
            return False, "Check Digit" + str(invalid) + "does not match calculated value" + str(i) + "."
        else:
            return True


if __name__ == "__main__":
    # main program
    studentID = input("Enter an ID ")
    get_check_digit(studentID)

    print("Main Program")
