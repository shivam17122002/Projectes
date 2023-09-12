import random

print("~~~~~~~~~~~~~~~~Welcom to our RPS~~~~~~~~~~~~~~~~~~~~\n")

user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name here: ")
print("""
Winning Rules:
1. Paper vs Rock ---> Paper
2. Rock vs Scissors ---> Rock
3. Scissors vs paper ---> Scissors\n""")

print("""Choices are:
1. Rock
2. Paper
3. Scissors""")
choice = int(input("Enter your choice number(1-3): "))
while choice > 3 or choice < 1:
   choice = int(input("Enter valid input: "))

if choice == 1:
  user_choice = "Rock"
elif  choice == 2:
  user_choice = "Paper"
else: 
  user_choice = "Scissors"
print("The user's choice is", user_choice)  
print(" ")
print("Now it is computer's turn")

computer = random.randint(1,3)

if(computer == 1):
  comp_choice = "Rock"
elif computer ==  2:
  comp_choice = "Paper"
else:
  comp_choice = "Scissors"

print("Computer's choice is:",comp_choice)
if((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
  print("Paper wins")
  result = "Paper"
elif ((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
  print("Rock wins")
  result = "Rock"
elif user_choice == comp_choice:
  print("it is tie")
  result = "Tie"
else:
  print("Scissors wins")
  result = "Scissor"

if result == "Tie":
  ties +=1
elif result == user_choice:
  print(name,"wins the match!")
  user_score +=1
else:
  print("Computer wins the match!")
  comp_score +=1

print("Scores are: ")
print(name,"'s score is", user_score)
print("Computer's score is", comp_score)
print("ties are",ties)
