import pytest
import TicTacTest

def test_evaluate():
    play = TicTacTest.evaluate('-------ooo----------')
    assert play == 1
    play2 = TicTacTest.evaluate('-------oxoxxox------')    
    assert play2 == 0
    play3 = TicTacTest.evaluate('oxoxoxoxoxoxoxoxoxox') 
    assert play3 == 1


def test_move_to_empty_space():
    board = TicTacTest.pc_move('--------------------')
    assert len(board) == 20
    assert board.count('o') == 1
    assert board.count('-') == 19

def test_move_failure():
    with pytest.raises(ValueError):
        TicTacTest.pc_move('oxoxoxoxoxoxoxoxoxox')

#What is a Python module and how does it differ from a Python package? 
# Module is a set of predefine functions. We can import module and den we can use functions from it. 
# Package is a bigger stracture, it is a set of modules. We import package like a module but when we want to use function from package we need to add submodule name 

#What are side effects and give some examples.
#It is when import of module run a action. It means that in module there is a function activated without our awarness
#side effects are when in package included function there are coments like: print, input, never ending loops

#What are Exceptions and what to do if third-party code that we use throws them?
# When in our code errors occure we can handle it with exception. Thanks that code is not terminated. 
# We receive special masage what happent and we can handle this exception by giving values to variables in this case
# If there is excetion we should read the massage and think if we would like to handle it 

#Using which keywords can you create, throw and catch your new custom Exception?
# try = "catch", raise = "create",  print = "throw"

#Give examples of some benefits of testing?
# If we test script we know if it run correctly in various situations
# We can try out script whitout adding additional command to the script code.
# Testing can be run atomaticly by design script and pytest
