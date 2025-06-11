import pytest
from calculator import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 8),    
    (-1, 1, 0),    
    (-5, -5, -10), 
    (2.5, 1.5, 4.0) 
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 3, 7),    
    (2, 5, -3),    
    (-5, -5, 0),  
    (5.5, 1.5, 4.0) 
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 4, 8),     
    (-3, 5, -15),
    (-2, -3, 6), 
    (0, 100, 0)  
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),   
    (5, 2, 2.5),  
    (-10, 2, -5),  
    (0, 5, 0) 
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)
