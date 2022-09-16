while True:
    print('\nWelcome to the Flarsheim Guesser!\n')
    print('Please think of a number between and including 1 and 100.\n')
    num1 = int(input('What is the remainder when your number is divided by 3?'))
    while True:
        if num1 < 0:
             print('The value enter must be 0 or greater')
        elif num1 >=3:
            print('The value entered must be less than 3')
        else:
            break
    while True:
        num2 = int(input('What is the remainder when your number is divided by 5?'))
        if num2 < 0:
            print('The value entered must be 0 or greater')
        elif num2 >=5:
            print('The value entered must be less than 5')
        else:
            break
    while True:
        num3 = int(input('What is the remainder when your number is divided by 7?'))
        if num3 < 0:
            print('The value entered must be 0 or greater')
        elif num3 >=7:
            print('The value entered must be less than 7')
        else:
            break
    for num in range(0, 101):
        if (num % 3 == num1 and num % 5 == num2 and num % 7 == num3):
            print('Your number was', num)
            print('How amazing was that?')
                  
    x = input('Do you want to play again? Y to continue, N to quit ==>')
    if x != ('y' or 'Y'):
        break
     
