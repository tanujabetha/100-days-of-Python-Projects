#Tip Calculator
billAmount = int(input("Enter the bill amount $:"))
TipPercent = int(input("Enter the tip percentage: "))
NumberofPersons = int(input("Enter the number of persons: "))
Share = (billAmount + (billAmount*(TipPercent/100)))/NumberofPersons
print(f"Each person should pay {Share}")