import random as rd
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

userInput = int(input("Enter the number:\n0 - rock\n1 - Paper\n2 - Scissors\n"))
computerInput = rd.randint(0,2)
rps = [rock, paper, scissors]
print(f"Computer chose \n {rps[computerInput]}")
print(f"You chose \n {rps[userInput]}")
#user winning condition
if (userInput == 0 and computerInput == 2) or (userInput == 1 and computerInput==0) or (userInput == 2 and computerInput == 1):
    print("You won")
elif (userInput == computerInput):
    print("Tie!")
else:
    print("You lose")
    
    
    
