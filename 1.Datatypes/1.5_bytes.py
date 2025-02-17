"""
Bytes data-type used to unify the string or other datatype in a unique encoding style
"""

def string_to_byte() -> None:
    """
    String to byte with 'utf-8' encoding
    Note: They are immutable
    return: None
    """
    name = "india"
    print(bytes(name,'utf-8')) # b'india'

def alter_string_to_byte() -> None:
    """
    Converts the other language string to byte
    return: None
    """
    name = "தமிழ்"
    print(bytes(name,'utf-8')) # b'\xe0\xae\xa4\xe0\xae\xae\xe0\xae\xbf\xe0\xae\xb4\xe0\xaf\x8d'

def string_to_byte_array() -> None:
    """
    Converts the string to byte array
    Note: they are mutable
    return: None
    """
    name = "india"
    name_as_byte_array = bytearray(name, 'utf-8')
    print(name_as_byte_array)  # b'india'

    # can perform list or array operation
    name_as_byte_array.reverse() # bytearray(b'india')
    print(name_as_byte_array) # bytearray(b'aidni')



if __name__ == "__main__":
    string_to_byte()
    alter_string_to_byte()
    string_to_byte_array()