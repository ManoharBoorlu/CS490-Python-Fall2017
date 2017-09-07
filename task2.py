import string                                    # import string function
alpha = set(string.ascii_lowercase)              # create a set of lowercase alphabets
string=input("Enter the String")
if((set(string.lower()) >= alpha)==True):        # If the set of input is greater than alphabets,then True.
    print("Contains all Alphabets")
else:
    print("Does not contain all Alphabets")
