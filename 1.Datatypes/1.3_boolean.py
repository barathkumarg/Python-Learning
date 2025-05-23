"""
About the boolean data-type python
"""

def bool_as_value() -> None:
    """
    Bool datatype described in terms of values, results of logical or arithmetic expressions
    :return: None
    """
    print("\nBoolean representation in values")
    print(10==9) #False
    print(1==1) #True

def bool_as_operator() -> None:
    """
    Can apply the bool function for the values of other datatype
    Return False -> In case of null or empty and True on other cases
    :return: None
    """
    print("\nBoolean representation in operator")
    print(bool(1)) #True
    print(bool(0)) #False
    print(bool("hello")) #True
    print(bool("")) #False
    print(bool([])) #False
    print(bool({})) #False

def bool_as_return_function() -> bool:
    """
    Boolean as a return type of the function
    :return: bool
    """
    print("\nBoolean representation as function return type")
    return True

if __name__ == "__main__":
    bool_as_value()
    bool_as_operator()
    print(bool_as_return_function())
