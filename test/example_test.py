#from app.example import enlarge

#def test_enlarge():
#    pass

from app.example import enlarge

def test_enlarge():
    #assert True
    #assert False
    #assert 2 == 2
    #assert 2 == 5
    assert enlarge(9) == 900

from app.example import to_usd
    
def test_to_usd():
    assert to_usd(1) == "$1.00"