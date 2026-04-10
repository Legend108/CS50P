from square import square

def test_positives():
    assert square(2) == 4
    assert square(3) == 9

def test_negatives():    
    assert square(-2) == 4   

def test_zero():
    assert square(0) == 0

def test_default():
    assert square() == "Enter a number."

def test_string():
    assert square("cat") == "Enter a number."

# This is meant to be used with pytest for checking testing different cases
