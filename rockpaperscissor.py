import random
player_choice=input("Enter rock or paper or scissor")
computer_choice=random.randstr("Rock, paper, scissor")
if player_choice=="Rock"and computer_choice=="Scissor":
    print("You win.")
elif player_choice=="Rock"and computer_choice=="Paper":
    print("You lose.")
elif player_choice=="Rock"and computer_choice=="Rock":
    print("Its a draw.")
elif player_choice=="Paper"and computer_choice=="Paper":
    print("Its a draw.")
elif player_choice=="Paper"and computer_choice=="Rock":
    print("You win.")
elif player_choice=="Paper"and computer_choice=="Scissor":
    print("You lose.")
elif player_choice=="Scissor"and computer_choice=="Paper":
    print("You win.")
elif player_choice=="Scissor"and computer_choice=="Rock":
    print("You lose.")
elif player_choice=="Scissor"and computer_choice=="Paper":
    print("Its a draw.")