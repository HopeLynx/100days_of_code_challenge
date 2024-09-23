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

choice_list = [rock,paper,scissors]

import random

pc_rand = random.randint(1,3) - 1
human_choice = int(input("Make your choice: where 1 - rock, 2 - paper, 3 - scissors: "))-1

print("Your choice:", choice_list[human_choice])
print("Computer choice:", choice_list[pc_rand])

if (human_choice == pc_rand):
    print("It's a draw.")
elif (human_choice == 0 and pc_rand == 2) or (human_choice == 1 and pc_rand == 0) or (human_choice == 2 and pc_rand == 1):
    print("You win!")
else:
    print("You lose...")