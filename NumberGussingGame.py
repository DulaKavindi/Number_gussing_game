#import math and random from librarys
import random
import math

def main():
    print("\nHELLO PLAYERS!\n")
    lower_number=int(input("\nEnter the lower bound:\n"))  #taking input for lower bound
    upper_number=int(input("\nEnter the upper bound:\n"))  #taking input for upper bound

    #generate a random number
    no=random.randint(lower_number,upper_number)  #No=random number

    #calculate the total chance
    total_chance=math.ceil(math.log2(upper_number-lower_number+1))

    print(f"\nYou have only {total_chance} chances to guess the correct number....\n")

    count=0
    flag=False

    while count<total_chance:
        count+=1

        guess=int(input("\nGuess a number:\n")) #guessing user's guess number as guess

        if no==guess:
            print("\nCongratulaton! you guess correct number.\n")
            print("\nNumber of attempt:\n",count)
            flag=True
            break
        elif no>guess:
            print("\nYour guess is too low!\n")
        else:
            print("\nYour guess is too high!\n")
    if not flag:
        print(f"\nThe number was {no}\n")
        print("\nBetter luck next time...\n")

if __name__=="__main__":
    main()