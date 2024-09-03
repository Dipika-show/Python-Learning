#write a program to read the text from a given file "poems.txt" and find out whether it contains the word twinkle
f = open("poems.txt")
content = f.read()

if ("twinkle" in content):
    print("the word twinkle is present in the file")
else:
    print("the word twinkle is not present in the file")    

f.close()