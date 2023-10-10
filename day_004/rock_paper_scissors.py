import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Hello! Welcome to this simple rock, paper, scissors game!")
player_choice = input("Type '0' for rock, '1' for paper and '2' for scissors.Good luck!\n")
player_choice = int(player_choice)

computer_choice = random.randint(0, 2)
print([rock, paper, scissors][player_choice])
print("Computer chose:")
print([rock, paper, scissors][computer_choice])

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == 0 and computer_choice == 1) or \
     (player_choice == 1 and computer_choice == 2) or \
     (player_choice == 2 and computer_choice == 0):
    print("Sorry, you lose!")
else:
    print("Well done, you win!")
