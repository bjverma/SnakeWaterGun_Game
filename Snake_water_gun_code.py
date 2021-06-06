#for the random selection of computer among snake, water and gun
#snake run inside water/ snake can drink water, so snake wins 
#gun can kill snake, so gun wins
#water can damage gun so water wins
import random
lst = ['s','w','g']

chance = int(input())
no_of_attempts = 0
computer_score = 0
player_score = 0

print("Welcome to Snake-Water-Gun Game\n")
print("type, s for snake \n type, w for water \n type, g for gun \n")


while no_of_attempts < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie: No points to both \n ")

    # if user enters s
    elif _input == "s" and _random == "g":
        computer_score = computer_score + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins: 1 point to computer\n")
        print(f"computer_score is {computer_score} and your point is {player_score} \n ")

    elif _input == "s" and _random == "w":
        player_score = player_score + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("player wins: 1 point to player \n")
        print(f"computer_score is {computer_score} and your point is {player_score} \n")

    # if user enters w
    elif _input == "w" and _random == "s":
        computer_score = computer_score + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins: 1 point to computer\n")
        print(f"computer_score is {computer_score} and your point is {player_score} \n ")

    elif _input == "w" and _random == "g":
        player_score = player_score + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("player wins: 1 point to player\n")
        print(f"computer_score is {computer_score} and your point is {player_score} \n")

    # if user enters g

    elif _input == "g" and _random == "s":
        player_score = player_score + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("player wins: 1 point to player\n")
        print(f"computer_score is {computer_score} and your point is {player_score} \n")


    elif _input == "g" and _random == "w":
        computer_score = computer_score + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins: 1 point to computer\n")
        print(f"computer_score is {computer_score} and your point is {player_score} \n ")

    else:
        print("you have input wrong \n")

    no_of_attempts = no_of_attempts + 1
    print(f"{chance - no_of_attempts} is left out of {chance} \n")

print("Game over")

if computer_score==player_score:
    print("Tie")

elif computer_score > player_score:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {player_score} and computer point is {computer_score}")



  
