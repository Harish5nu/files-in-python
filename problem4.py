#Q4. A file contains a word "Donkey" mutltiple times. You need to write a program which replace this word with ##### by updating the same file.
word="Donkey"

with open("file.txt", "r") as f:
    content=f.read()
contentnew=content.replace(word,"######")

with open("file.txt","w") as f:
    f.write(contentnew)