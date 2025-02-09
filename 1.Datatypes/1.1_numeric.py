"""
Explains about the Numeric Python data types
"""
import math

def integer():
    """
    Integer Datatypes and their operations
    """
    num_ten = 10
    num_five = 5
    print("*** Numeric DataType ***")
    print(f"Type of the variable: {type(num_ten)}") # <class int>

    # OPERATIONS
    # Addition, Subtraction
    print(f"Add : {num_ten + num_five}, Subtract : {num_ten - num_five} ") # 15, 5

    # Multiplication, Division
    print(f"Multiply: {num_ten * num_five}, Divide: {num_ten / num_five}") # 50, 2.0

    # Floor division (return int result on division)
    print(f"Floor division: {num_ten // num_five}") # 2

    # Modulus and square
    print(f"Modulus: {num_ten % num_five}, Square: {num_ten ** 2}") # 0, 100

    # Absolute and round off
    print(f"Absolute: {abs(-10)}, Roundoff: {round(2.134,2)}") # 10, 2.13

def float():
    """
    Float Datatypes and their operations
    """
    num_ten = 10.0
    num_five = 5.0
    print("\n*** Float DataType ***")
    print(f"Type of the variable: {type(num_ten)}") # <class float>

    # OPERATIONS
    # Addition, Subtraction
    print(f"Add : {num_ten + num_five}, Subtract : {num_ten - num_five} ") # 15.0, 5.0

    # Multiplication, Division
    print(f"Multiply: {num_ten * num_five}, Divide: {num_ten / num_five}") # 50.0, 2.0

    # Floor division (return int result on division, exception on float case)
    print(f"Floor division: {num_ten // num_five}") # 2.0

    # Modulus and square
    print(f"Modulus: {num_ten % num_five}, Square: {num_ten ** 2}") # 0.0, 100.0

    # Absolute and round off
    print(f"Absolute: {abs(-10)}, Roundoff: {round(2.134,2)}") # 10, 2.13

def complex():

    """
    Complex Datatypes and their operations
    """
    num_ten = 10 + 5j
    num_five = 5 + 1j
    print("\n*** Complex DataType ***")
    print(f"Type of the variable: {type(num_ten)}")  # <class , complex>

    # OPERATIONS
    # Addition, Subtraction
    print(f"Add : {num_ten + num_five}, Subtract : {num_ten - num_five} ")  # 15 + 6j , 5 + 4j

    # Multiplication, Division
    print(f"Multiply: {num_ten * num_five}, Divide: {num_ten / num_five}")  # 45 + 35j , 2 + 0.5j

    # Square
    print(f"Square: {num_five ** 2}") # 24 + 10j

    # Conjugate
    print(f"Conjugate: {num_five.conjugate()}") # 5 - 1j

    # Fetch the real and imaginary part, treated as float type
    print(f"Real: {num_five.real}, Imaginary: {num_five.imag}")

def special_notation():
    """
    Nan and infinity was marked as
    """
    print("\nSpecial Notations")

    NAN = math.nan
    print(NAN)

    # Infinity and -Infinity Example
    INF = math.inf
    MINF = -math.inf
    print(INF)
    print(MINF)

if __name__ == "__main__":
    integer()
    float()
    complex()
    special_notation()