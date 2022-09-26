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

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    play = input('Do you want to play again? ==>')          #This function asks the user for a yes or no input.
    while (play.upper() != 'YES') and (play.upper() != 'Y') and (play.upper() != 'NO') and (play.upper() != 'N'):
        print('Please try again.')                          #If acceptable input isn't entered then the user will be asked to try again.
        play = input('Do you want to play again?')
    if (play.upper() == 'YES') or (play.upper() == 'Y'):
        return True
    elif (play.upper() == 'NO') or (play.upper() == 'N'):
        return False
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    bank = int(input('How many chips do you want to wager? ==>'))
    if bank < 0:                                                    #If input is out of range, then user will be asked again.
        print('Too low a value, you can only choose 1-100 chips')
    elif bank > 100:
        print('Too high a value, you can only choose 1-100 chips')
    else:
        print(bank)
    return bank            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    
    return random.randint(1,10), random.randint(1,10), random.randint(1,10)

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reela == reelc:               #Tells how many reels matched, if any.
        return 
    elif reela == reelb and reela != reelc:
        return 2
    elif reela == reelc and reela != reelb:
        return 2
    elif reelb == reelc and reelb != reela:
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    start = int(input('How many chips do you want to start with? ==>'))     #Wager must be in range or below what is in the bank.
    if start < 0:
        print('The wager amount must be greater than 0. Please start again.')
    elif start > 100:
        print('The wager amount must be less than 100. Please start again.')
    elif start > start:
        print('The wager amount can not be greater than how much you have.')
    return start

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    matches = get_matches(reela, reelb, reelc)
    if matches == 3:                                        #Multiples wager to show winnings or losings.
        return wager *10
    elif matches == 2:
        return wager *3
    else:
        return wager *-1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank > 0:
          
            
            wager = get_wager(bank)

            reela, reelb, reelc = get_slot_results()

            matches = get_matches(reela, reelb, reelc)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reela, reelb, reelc)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()

