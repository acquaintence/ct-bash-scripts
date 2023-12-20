import random


print("\n⋆ ˙ ⟡ ♡ Rock Paper Scissors ⋆ ˙ ⟡ ♡ ")
actions = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
play = True
while play == True:

    prompt = input("\nWould you like to play? y/n ")
    if prompt.lower() == "y":
        response = True 
        while response == True:
            player_action = input("\nRock / Paper / Scissors ? ")
            if player_action.lower() in actions:
                response = False
                computer_action = random.choice(actions)
                print(f"\nYou chose {player_action}. Computer chose {computer_action}. ")

                if player_action == computer_action:
                    print(f"Both players selected {player_action}. It's a tie!")
                elif player_action == "rock":
                    if computer_action == "scissors":
                        print("Rock smashes scissors! You win!")
                        player_score += 1
                    else:
                        print("Paper covers rock! You lose.")
                        computer_score += 1
                elif player_action == "paper":
                    if computer_action == "rock":
                        print("Paper covers rock! You win!")
                        player_score += 1
                    else:
                        print("Scissors cuts paper! You lose.")
                        computer_score += 1
                elif player_action == "scissors":
                    if computer_action == "paper":
                        print("Scissors cuts paper! You win!")
                        player_score += 1
                    else:
                        print("Rock smashes scissors! You lose.")
                        computer_score += 1
                
                print(f"\n\t Score: \n\t - Player: {player_score} \n\t - Computer: {computer_score}")

            else: 
                print("Invalid response, please try again.")
                response = True


    elif prompt.lower() == "n":
        print("\nOkie doke. Thanks for playing. ")
        print(f"\n\t Final Score: \n\t - Player: {player_score} \n\t - Computer: {computer_score}")
        if player_score == computer_score:
            print("\nIt's a tie!")
        elif player_score > computer_score:
            print("\nYou Win!")
        else: 
            print("\nYou Lose!")
        print(""" 
  ૮_‘_ა   
૮˶• ﻌ •˶ა
./づ~ ♡ bye bye ♡ 
              """)


        play = False

    else:
        print("Invalid response, please select y/n ")


