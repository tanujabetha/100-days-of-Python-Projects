print("Welcome to Treasure Island.Your mission is to find the treasure")
direction = input("Choose direction you want to go to (left or right)").lower()
if direction == "left":
    swim_wait = input("Do you want to swim or wait: ").lower()
    if(swim_wait == "wait"):
        door = input("Choose the door: (Red, blue, Yellow or anything)").lower()
        if door == "red":
            print("Burned by fire.\nGame Over.")
        elif door == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif door == "yellow":
            print("You Win!!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")
        

