import time
import random
import sys

rules ="""
Welcome to the snake and ladder game.
    Rules:
      1. Initally all the players are at starting position i.e. 0. 
         Take it in turns to roll the dice. 
         Move forward the number of spaces shown on the dice.
      2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
      3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
      4. The first player to get to the FINAL position is the winner.
      5. Hit enter to roll the dice.

    """

# This function will get player names and number of players.
def players():
    while True:
        player_number = (input("Maximum 6 players can play the game. Enter No. of Players:"))
        if player_number.isdigit() and 7>int(player_number)>0:
            player_number = int(player_number)
            break

    player_names  = []
    for num in range(player_number):
        player = None
        while not player:
            player = input("Please enter a valid name: ").strip()
        player_names.append(player)

    print("Players participating in the match are:\n",*player_names,sep = "\n")
    return player_names

#Roll_dice is will return value between 1 and 6
def roll_dice():
    dice_value = random.randint(1, 6)
    time.sleep(1)
    print("Its a " + str(dice_value))
    return dice_value

# snakes will move you down from key to value
snakes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}

# ladder takes you up from 'key' to 'value' 
ladders = {
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}

player_turn_text = [
    "Your turn.",
    "Please proceed.",
    "Lets win this.",
    "Are you ready?"
]

snake_bite = [
    "boohoo",
    "bummer",
    "snake bite",
    "oh no",
    "dang"
]

ladder_jump = [
    "woohoo",
    "woww",
    "nailed it",
    "oh my God...",
    "yaayyy"
]


#This function will move down the snake
def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


#This function will move player on ladder
def get_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


#This function will return final value after every turn
#The value will be checked for snake and ladders
def snake_ladder_main(player_name, current_value, dice_value):
    time.sleep(1)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > 100 :
        print("You need " + str(100 - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        get_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value

# This function will check for the winner and end the game

def check_win(player_name, position):
    time.sleep(1)
    if position == 100:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.")
        sys.exit(1)


    

def main():
    print(rules)
    time.sleep(2)
    player_name = players()

    current_value ={}
    for i in range(len(player_name)):
        current_value.update({i:0})

    while True:
        for i in range(len(player_name)):
        
            time.sleep(1)
            sys.stdin.flush()
            input_enter = input("\n" + player_name[i] + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
            dice_value = roll_dice()
            print("\n Rollling dice ........")
            time.sleep(1)
            player_current_position = snake_ladder_main(player_name[i], current_value[i], dice_value)
            current_value.update({i:player_current_position})
            check_win(player_name[i], player_current_position)


if __name__ == "__main__":
    main()
