
dictonary = {"name" :"barath" ,"rollno" :17892}

def dictonary_methods():
    """ Basic dictionary functions """

    # Get the value
    print(dictonary.get("name")) # barath

    # Add the new key
    dictonary["dept"] = "cse" # adds the new key in dictionary {"name":"barath","rollno":17892,"dept":"cse}

    # delete the key
    dictonary.pop("dept") # {"name" :"barath" ,"rollno" :17892}

    # iterate the keys and value
    print([(key, value) for key,value in dictonary.items()])  # [('name', 'barath'), ('rollno', 17892)]


if __name__ == "__main__":
    dictonary_methods()
