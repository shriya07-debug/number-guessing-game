def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def product(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return 'it cannot be divided'
    return x/y

def power(x,y):
    return x**y

def square(x):
    return x**2 

while True:
    print("the choices are listed below: ")
    print('1, add')
    print('2, subtract')
    print('3, multiply')
    print('4, divide')
    print('5, power')
    print('6, square')
    print('7, to exit')

    user_choice=int(input("enter one choice from above: "))
    if user_choice==7:
        print("you have exited the calculator")
        break


    n1=float(input("enter the first number: "))
    n2=float(input("enter the second number: "))
   

    if user_choice==1:
        print(add(n1,n2))
    
    elif user_choice==2:
        print(subtract(n1,n2))
    
    elif user_choice==3:
        print(product(n1,n2))
    
    elif user_choice==4:
        print(divide(n1,n2))

    elif user_choice==5:
        print(power(n1,n2))
    
    elif user_choice==6:
        print(square(n1))

    else:
        print("the choice you have entered it incorrect!!")
    

