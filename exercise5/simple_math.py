"""
A collection of simple math operations 
""" 

def simple_add(a,b):
    """Add to numbers together.
        
    It works for any two compatible datatypes which support the + operation.
    
    Parameters
    ----------
    a : int, float, etc...
        First number in the addition operation.
    b : int, float, etc...
        Second number in the addition operation.
    
    Returns
    -------
    int, float
        The result of the addition, in the datatype compatible with the inputs.
        
    Examples
    --------
    >>> simple_math.add(1, 2)
    3
    """
    return a+b

def simple_sub(a,b):
    """Substract a number from another.
    
    It works for any two compatible datatypes which support the - operation.
    
    Parameters
    ----------
    a : int, float, etc...
        First number in the subtraction operation.
    b : int, float, etc...
        Second number in the subtraction operation.
    
    Returns
    -------
    int, float
        The result of the subtraction, in the datatype compatible with the inputs.
        
    Examples
    --------
    >>> simple_math.sub(1, 2)
    -1
    """
    return a-b

def simple_mult(a,b):
    """Multiply two numbers.
    
    It works for any two compatible datatypes which support the * operation.
    
    Parameters
    ----------
    a : int, float, etc...
        First number in the multiplication operation.
    b : int, float, etc...
        Second number in the multiplication operation.
    
    Returns
    -------
    int, float
        The result of the multiplication, in the datatype compatible with the inputs.
        
    Examples
    --------
    >>> simple_math.mult(1, 2)
    2
    """
    return a*b

def simple_div(a,b):
    """Divide two numbers.
    
    It works for any two compatible datatypes which support the / operation.
    .. warning:: This method does not check if the divisor is zero. This will probably cause a crash if a value of zero is supplied.
    
    Parameters
    ----------
    a : int, float, etc...
        First number in the division operation.
    b : int, float, etc...
        Second number in the division operation.
    
    Returns
    -------
    int, float
        The result of the division, in the datatype compatible with the inputs.
        
    Examples
    --------
    >>> simple_math.div(6, 2)
    3
    """
    return a/b

def poly_first(x, a0, a1):
    """Calculate a first order polynomial.
    
    It works for any two compatible datatypes which support the + and * operations.
    
    Parameters
    ----------
    x : int, float, etc...
        The polynomial variable.
    a0 : int, float, etc...
        The constant factor in the polynomial.
    a1 : int, float, etc...
        The linear factor in the polynomial.
    
    Returns
    -------
    int, float
        The polynomial with factors a0 and a1, evaluated at x, in the datatype compatible with the inputs.
        
    Examples
    --------
    >>> simple_math.poly_first(2, 2, 3)
    8
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """Calculate a second order polynomial.
    
    It works for any two compatible datatypes which support the + and * operations.
    
    Parameters
    ----------
    x : int, float, etc...
        The polynomial variable.
    a0 : int, float, etc...
        The constant factor in the polynomial.
    a1 : int, float, etc...
        The linear factor in the polynomial.
    a1 : int, float, etc...
        The quadratic factor in the polynomial.
    
    Returns
    -------
    int, float
        The polynomial with factors a0, a1 and a2, evaluated at x, in the datatype compatible with the inputs.
        
    Examples
    --------
    >>> simple_math.poly_second(2, 2, 3, 5)
    28
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....

def factorial(n):
    """Calculate the factorial of a positive integer.
    
    It takes in a positive integer as an input and returns its factorial.
    .. warning:: This method does not check if the input is a positive integer. The program will enter an infinite loop if a negative integer or a non-integer number is supplied.
    
    Parameters
    ----------
    n : int
        The integer that we want to calculate the factorial of.
    
    Returns
    -------
    int
        The factorial of n.
        
    Examples
    --------
    >>> simple_math.factorial(10)
    3628800
    """
    if n==0: return 1
    return n*factorial(n-1)

def exp(x):
    """Calculate the exponential of a number.
    
    This method calculates the exponential of a number by approximating it by the sum of the 30 first terms of the taylor expansion.
    It works for any datatype which supports the + and * operations.
    
    Parameters
    ----------
    x : int, float
        The number that we want to calculate the exponential of.
    
    Returns
    -------
    float
        The exponential of x.
        
    Examples
    --------
    >>> simple_math.exp(10)
    22026.460266271286
    """
    N = 30
    x = float(x)
    return sum([(x)**n/(factorial(n)) for n in range(N)])