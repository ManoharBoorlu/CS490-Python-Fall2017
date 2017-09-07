file=open("examplefile.txt","r")          # Opening the File in Read mode
count={}                                  # Creating a Dictionary
for word in file.read().split():          # Loop for Splitting words
    if word not in count:
        count[word] = 1                   # If word is not in dictionary, then add it else increase the count
    else:
        count[word] += 1
print (word,count)
file.close();
