
# TODO: import some code

# TODO: test the code

from app.game import determine_winner

def test_determine_winner():
    assert determine_winner(user_choice="rock", computer_choice="paper") == "paper"