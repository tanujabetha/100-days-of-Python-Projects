import random as rd

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_List = []
computer_List = []

def randomDrawCards(List, number):
    """ Adding the cards into the list randomly
    """
    for i in range(number):
        card = rd.choice(cards)
        List.append(card)

def calculate_Score(List):
    """Calculating the sums of the lists"""
    return sum(List)

def computerCardsDrawing(computerSum):
    while computerSum <= 16:
        randomDrawCards(computer_List, 1)
        computerSum = calculate_Score(computer_List)
    return computerSum

def usercardsDrawing(userSum):
    userChoice = input("User! Do you want to continue drawing the cards: (Y or N)").lower()
    while userChoice == 'y':
        randomDrawCards(user_List, 1)
        userSum = calculate_Score(user_List)
        print(f"Your cards now are: {user_List} with sum {userSum}")
        if userSum > 21:
            return userSum
        userChoice = input("User! Do you like to draw more cards: (Y or N) ").lower()
    return userSum

def main():
    global user_List, computer_List
    # Initial Draws
    randomDrawCards(user_List, 2)
    randomDrawCards(computer_List, 2)
    # Getting the sum
    userSum = calculate_Score(user_List)
    computerSum = calculate_Score(computer_List)
    # Displaying the sum and the computer's data to the user
    print(f"Hey! These are your cards:{user_List} with sum {userSum}")
    print(f"Hey User! This is one of the computer's card: {computer_List[0]}")
    if userSum < 21:
        userSum = usercardsDrawing(userSum)
    if userSum <= 21:
        computerSum = computerCardsDrawing(computerSum)
    userSumDiff = 21 - userSum
    computerSumDiff = 21 - computerSum
    if userSum > 21:
        print("You lost! It is a bust!!!!!!")
    elif computerSum > 21 or userSumDiff < computerSumDiff:
        print(f"Congrats User! You won with cards {user_List} with sum {userSum}\n")
    elif userSum == computerSum:
        print("It is a draw!!")
    else:
        print(f"Computer Won! with cards {computer_List} with sum {computerSum}\n")
    print(f"The users cards: {user_List} with sum {userSum}")
    print(f"The computers cards: {computer_List} with sum {computerSum}")

if __name__ == "__main__":
    main()
