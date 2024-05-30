import random


def rsp():
    hands = ["rock", "scissor", "paper"]
    com_hand = random.choice(hands)
    user_hand = input("Enter your hand: ").lower().strip()

    if user_hand == com_hand:
        print("draw")
    elif (user_hand == "rock" and com_hand == "paper") or (user_hand == "scissor" and com_hand == "paper") or (user_hand == "rock" and com_hand == "scissor") or (user_hand == "paper" and com_hand == "rock"):
        print("You win!")

    else:
        print("You lose!")


rsp()

play_again = input("Wanna play again? ").lower()
while play_again != "no":
    rsp()
    play_again = input("Wanna play again? ").lower()
