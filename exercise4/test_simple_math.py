import simple_math
import numpy as np

def test_simple_add():
    assert simple_math.simple_add(1,1) == 2
    
def test_simple_sub():
    assert simple_math.simple_sub(3,2) == 1
    
def test_simple_mult():
    assert simple_math.simple_mult(2,2) == 4
    
def test_simple_div():
    assert simple_math.simple_div(3,2) == 1.5
    
def test_poly_first():
    x = 2.456
    a0 = 3.451
    a1 = 6.123
    assert simple_math.poly_first(x, a0, a1) == a0 + a1*x
    
def test_poly_second():
    x = 2.456
    a0 = 3.451
    a1 = 6.123
    a2 = 8.161
    assert simple_math.poly_second(x, a0, a1, a2) == a0 + a1*x + a2*(x**2)
    
def test_factorial():
    assert simple_math.factorial(10) == 3628800
    
def test_exp():
    eps = 1E-3
    x = 4.123
    assert abs(simple_math.exp(x) - np.exp(x)) < eps