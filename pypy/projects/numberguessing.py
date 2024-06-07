import random
import math
#guessing number game python
#taking inputs
lower = int(input("Enter lower number "))
upper = int(input("Enter highest number "))
#generating random number between lower and upper
x = random.randint(lower,upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), "chances to guess the number \n")

#initializing the number of counts
count = 0

while count < math.log(upper - lower + 1, 2):
    count +=1

    #taking guessing number as input
    guess = int(input("Guess a number: - "))

    #condition testing
    if x == guess:
        print("Congrats you did it in", count," try")
        break
    elif x> guess:
        print("You guessed too small")
    elif x < guess:
        print("You guessed too high!")

if count >= math.log(upper - lower +1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")