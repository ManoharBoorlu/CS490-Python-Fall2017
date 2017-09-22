str = input("Enter Sentence")
list = []
for word in str.split():
    if word not in list:
        list.append(word)
str1 = ' '.join(sorted(list))
print((str1))
