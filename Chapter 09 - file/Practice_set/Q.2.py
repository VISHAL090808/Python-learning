import random

def game():
    print('You are playing game')
    score= random.randint(1, 50)
    #fetch the score
    with open(r'd:\Python\Chapter 09 - file\Practice_set\highscore.txt') as f:
        highscore= f.read()
        if( highscore !=''):
            highscore= int(highscore)
        else:
            highscore = 0

    print('your score :', score)

    if(score> highscore):
        #updating highscore
        with open(r'd:\Python\Chapter 09 - file\Practice_set\highscore.txt', 'w') as f:
            f.write(str(score))
    return score

game()