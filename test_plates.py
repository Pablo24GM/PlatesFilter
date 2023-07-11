import plates

def test_con_1():   # plate must have between 2 and 6 characters #
    assert plates.is_valid('A') == False
    assert plates.is_valid('AA') == True
    assert plates.is_valid('AAAAAA') == True
    assert plates.is_valid('AAAAAAA') == False

def test_con_2():   # plate must only have letters and numbers #
    assert plates.is_valid('ABCDEF') == True
    assert plates.is_valid('123456') == False
    assert plates.is_valid('ABC123') == True
    assert plates.is_valid('ABC+/%') == False

def test_con_3():   # plate stars with at least 2 letters #
    assert plates.is_valid('ABC') == True
    assert plates.is_valid('ABC123') == True
    assert plates.is_valid('AB12') == True
    assert plates.is_valid('123') == False
    assert plates.is_valid('123ABC') == False
    assert plates.is_valid('12AB') == False

def test_con_4():   # plate must end with numbers if they contain any number #
    assert plates.is_valid('AB') == True
    assert plates.is_valid('ABC') == True
    assert plates.is_valid('ABCD') == True
    assert plates.is_valid('ABCDE') == True
    assert plates.is_valid('ABCDEF') == True
    assert plates.is_valid('AB1') == True
    assert plates.is_valid('AB12') == True
    assert plates.is_valid('AB123') == True
    assert plates.is_valid('AB1234') == True
    assert plates.is_valid('ABC1') == True
    assert plates.is_valid('ABC12') == True
    assert plates.is_valid('ABC123') == True
    assert plates.is_valid('ABCD1') == True
    assert plates.is_valid('ABCD12') == True
    assert plates.is_valid('ABCDE1') == True
    assert plates.is_valid('AB1C') == False
    assert plates.is_valid('AB1CD') == False
    assert plates.is_valid('AB1CDE') == False
    assert plates.is_valid('AB12CD') == False
    assert plates.is_valid('AB123C') == False

def test_con_5():   # plate numbers must not start with 0 #
    assert plates.is_valid('AB') == True
    assert plates.is_valid('ABCDEF') == True
    assert plates.is_valid('AB1234') == True
    assert plates.is_valid('AB0123') == False
    assert plates.is_valid('ABC123') == True
    assert plates.is_valid('ABCD12') == True
    assert plates.is_valid('ABCDE1') == True