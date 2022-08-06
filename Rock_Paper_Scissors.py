import random

choices = ['rock', 'paper', 'scissors']
randchoice = (random.choice(choices))



def play():
    ''' This is play Game function '''
    userInput = input("Enter rock,paper and scissors: ")
    if userInput == randchoice:
        print('You Won')
    else:
        print("You lost")


if __name__ == "__main__":
    while (True):
        inp = input("Enter Command 'play' to play or press any key to exit: ")
        if inp == 'play':
            play()
        else:
            print("Thank you for playing Game")
            break
