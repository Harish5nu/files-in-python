#Q> The game fucntion in a program lets a user play a game and returns the score as an interger.
# You need to read the file 'Hi-score.txt' which is either blank or contains the previous Hi-score .
# You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
import random

def game():
    print("You are playing the game...")
    score=random.randint(1,62)
    #fetch the hiscore
    with open("hiscore.txt") as f :
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    
    print(f"Your score: {score}")
    if(score>hiscore or hiscore==""):
        # write this hiscore to the file.
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score

game()