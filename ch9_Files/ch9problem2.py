#the game{} function in a program lets a user play a game and returns the score as an integer.you need to read a file 

import random
def game():
    print("you are playing a game..")
    score =  random.randint(1,100)
    #fetch the highscore
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore !=""):
            hiscore=int(hiscore)
        else:
            hiscore=0

    print(f"your score is:{score}")
    if(score>hiscore):
    #write this hiscore to the file
      with open("hiscore.txt","w") as f:
       f.write(str(score))



    return score
game()