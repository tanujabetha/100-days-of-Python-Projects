#First generate a random word from lists of words
#A string with empty data
#Until user guesses the word or hangman die, we must repeat the below steps
#Asking user to guess a letter
    #if the letter in the list, update the index of blank with letter and show the user the blanked strings
    # if the letter is not in list, show that man is losing a part and going to die
import random as rd
wordsList = ["Apple","narcissistic","oblivious","calm","chocolate","waffle","bottle","book","eyedrops"]
HangMan_state = [
    r'''+---+
    |   |
        |
        |
        |
        |
=========''',

    r'''+---+
    |   |
    O   |
        |
        |
        |
=========''',

    r'''  +---+
    |   |
    O   |
    |   |
        |
        |
=========''',

    r'''  +---+
    |   |
    O   |
   /|   |
        |
        |
=========''',

    r'''  +---+
    |   |
    O   |
   /|\  |
        |
        |
=========''',

    r''' +---+
    |   |
    O |
   /|\ |
   /    |
        |
=========''',

    r''' +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
========='''
]

word = rd.choice(wordsList)
word = list(word)
#print(word)
blankword = ""
for blankcount in range(0,len(word)):
    blankword+='_'
blankword = list(blankword)
countBlankWord = len(word)
end_of_game = False
hangman = 0
letterIteration = 0
print(f"The word has : {blankword}")
while not end_of_game:
    userInput = input("Enter the letter you think is in the word: ").lower()
    letterIteration = 0
    for charIndex in range(0,len(word)):
        if word[charIndex] == userInput:
            blankword[charIndex] = userInput
            letterIteration = 1
    if "_" not in blankword:
        end_of_game = True
        print(f"You win! The word is : {blankword}")
        break
    if letterIteration == 0:
        hangman+=1
        print(HangMan_state[hangman])
        if hangman >=6:
                print(f"You Lose! The word was {word}")
                break
    print(blankword)
