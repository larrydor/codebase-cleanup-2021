from random import choice
def determine_winner(user_choice, computer_choice):
    return "paper"
if __name__ == "__main__":
    # STILL ALLOW US TO RUN FROM COMMAND LINE
    # AND DO THE STUFF BELOW
    # BUT NOT DO THE STUFF BELOW WHEN TRYING TO IMPORT
    # IN ORDER FOR US TO BE ABLE TO IMPORT ANY FUNCTION
    # ... FROM ANY FILE (LIKE THIS ONE)
    # ... THIS FILE NEEDS A CLEAN GLOBAL SCOPE
    # ... (ONLY FUNCTIONS AND A MAIN CONDITIONAL)
    #
    # USER SELECTION
    #
    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in ["rock", "paper", "scissors"]:
        print("OOPS, TRY AGAIN")
        exit()
    #
    # COMPUTER SELECTION
    #
    c = choice(["rock", "paper", "scissors"])
    print("COMPUTER CHOICE:", c)
    #
    # DETERMINATION OF WINNER
    #
    if u == "rock" and c == "rock":
        print("It's a tie!")
    elif u == "rock" and c == "paper":
        print("The computer wins")
    elif u == "rock" and c == "scissors":
        print("The user wins")
    elif u == "paper" and c == "rock":
        print("The computer wins")
    elif u == "paper" and c == "paper":
        print("It's a tie!")
    elif u == "paper" and c == "scissors":
        print("The user wins")
    elif u == "scissors" and c == "rock":
        print("The computer wins")
    elif u == "scissors" and c == "paper":
        print("The user wins")
    elif u == "scissors" and c == "scissors":
        print("It's a tie!")