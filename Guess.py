import random

number = random.randint(1,10)
def intro():
    print("May i ask for your name: ")
    global name
    name = input()
    print(name + ",we are going to play a game, i am thinking of a number between 1 and 10")

    if number%2 == 0:
        x='even'
    else:
        x='odd'
        print("\nThis is an {} number".format(x))
        print("go ahead guess")


def pick():
    guesstaken = 0
    while guesstaken < 5:
        enter = input("guess: ")


        try: 

            guess = int(enter)

            if guess<=10 and guess>=1:
                guesstaken = guesstaken + 1
                if guesstaken <5:
                    if guess<number:
                        print("the number that you entered is too low: ")
                    if guess>number:
                        print("the number you entered is too high")
                    if guess!= number:
                        print("try again")
                    if guess== number:
                        break
            if guess>10 or guess<1:
                print("that number isn't in the range! ")

                print("Please enter a number between 1 and 10")

        except:
            print("I dont think that "+enter+" is a number. Sorry")

    if guess == number:
        guesstaken = str(guesstaken)
        print('good job,{}! you guessed my number in {} guesses!'.format(name,guesstaken))
    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))
playagain = 'yes'
while playagain == 'yes' or playagain == 'y' or playagain == 'Yes':
    intro()
    pick()
    print('do you want to play again')
    playagain = input()

