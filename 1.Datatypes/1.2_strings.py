def stringOperations():
    """Basic Operations of Strings"""
    
    strValue = "Hello World!"
    print(strValue) #Hello World!
    
    print("hello \"python\" world ") # to print with double quotes, you can use escape characters
    
    multilineString= '''This
is a
multilineString''' 
    print(multilineString)#This
    # is a
    # multilineString
    
    for i in strValue: # Looping string characters
        print(i, end='')
    print()
    print(len(strValue)) #Length of string: 12
    
    print("Hello" in strValue) #check whether occurance of text: True
    
    print("Hi" not in strValue) # True
    
    #Slicing
    print(strValue[6:]) #World!
    print(strValue[0:5]) #Hello
    print(strValue[-6:-1]) #World
    
    
    #Modify
    print(strValue.upper())
    print(strValue.lower())
    print(strValue.strip()) # removes whitespace in  before or after string
    print(strValue.replace('l','Y')) #replaces all the character of string
    print(strValue.split(' '))  #splits the string into substring
    
if __name__ == "__main__":
    stringOperations()
