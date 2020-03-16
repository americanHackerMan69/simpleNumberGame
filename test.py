import random
import time

print("Welcome to Nicholas's Random Number game!")
print("")
raw_input("Press any key to continue....")

number = random.randint(1,100)
chances = 5

a = input("From 1 to 100, what is the number?: ")

if a>100:
    while True:
       print("YOU CANT GUESS ABOVE 100!!!")
       a = input("From 1 to 100, what is the number?: ")
       if a<101:
           break

if a < 1:
    while True:
        print("YOU CANT GUESS BELOW 1!!!!")
        a = input("From 1 to 100, what is the number?: ")
        if a>0:
            break

if a==number:
    print("CORRECT. You win!")
if a!=number:
    chances = chances - 1
    while True:
        print("WRONG! You have " + str(chances) + " chances left")
        chances = chances -1
        a = input("From 1 to 100, what is the number?: ")
        if a < 1:
            while True:
                print("YOU CANT GUESS BELOW 1!!!!")
                a = input("From 1 to 100, what is the number?: ")
                if a > 0:
                    break
        if a > 100:
            while True:
                print("YOU CANT GUESS ABOVE 100!!!")
                a = input("From 1 to 100, what is the number?: ")
                if a < 101:
                    break
        if a == number:
            print("CORRECT. You win!")
            break
        if chances == 0 and a!=number:
            print("WRONG! You lose! The real nunber was " + str(number))
            break




