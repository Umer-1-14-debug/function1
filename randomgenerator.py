import random
playing=True
number=int(random.randint(10, 20))
guess=int(input("Guess the number\n"))
while playing:
    if number==guess:
        print("You have guessed it")
        print("Well done, You have guessed the number ",number)
    else:
        print("Wrong number. Try again.")