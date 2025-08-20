import random as rn
number=rn.randint(1,100)

while True:
    user_guess=int(input('enter your guess: '))

    if user_guess==number:
        print("you have guessed the number: ")
        user_choice=input("do you want to continue?")
        if user_choice=='yes':
            number=rn.randint(1,100)
            continue
        elif user_choice=='no':
            print("you have exited the game")
            break
        
    elif user_guess<number:
        print("guess higher")
    
    elif user_guess>number:
        print("guess lower")
    
    else:
        print("invalid guess")
        