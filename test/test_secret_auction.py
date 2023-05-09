import sys
from os.path import abspath, dirname

# Add the parent directory of the current file to sys.path
sys.path.append(abspath(dirname(dirname(__file__))))

from src import secret_auction

def test_find_winner():
    player_dict = {
        "Douglas" : 100,
        "Tayla" : 120,
        "Pandora" : 119,
        "Shiva" : 120
    }
    assert secret_auction.find_winner(player_dict) == "Tayla"

