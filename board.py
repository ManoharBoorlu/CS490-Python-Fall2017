def draw(h,w):                                         # Function for drawing
    str1=" ----"
    str2="|    "
    for i in range(h):                                 # Forloop within range of height
        print(str1*w + '\n' + str2*w + '|')            # Printing the Strings
    print(str1*w)                                      # Printing the last line

h = int(input("Enter the height of the board: "))
w = int(input("Enter the width of the board: "))
draw(h,w)








