import random as rd
letter = int(input("Enter the number of letters: "))
numbers = int(input("Enter the number of numericals: "))
specialChar = int(input("Enter the number of special characters: "))
letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
specialCharList = ['!', '"','#', '$', '%', '&', '(', ')', '*', '+']
numbersList = ['1','2','3','4','5','6','7','8','9','0']
i = 0
finalString = ""
#rd.choice(list) - it gives the a random item from the list
#for r in range (0,letter+1):
while i<letter:
     s = letterList[rd.randint(0,len(letterList)-1)]
     i = i+ 1
     finalString += s
i=0
while i<numbers:
     s = numbersList[rd.randint(0,len(numbersList)-1)]
     i = i+ 1
     finalString += s
i=0
while i<specialChar:
    s = specialCharList[rd.randint(0,len(numbersList)-1)]
    i = i+1
    finalString +=s
#Random.shuffle() needs a list. So we convert string into list and the  use join to make it to string again
fstring = list(finalString)
rd.shuffle(fstring)
#print(fstring)
print (''.join(fstring))
     
     