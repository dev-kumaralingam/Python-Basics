import datetime
def greetuser():
    current_time=datetime.datetime.now()
    hour=current_time.hour
    if hour<12:
        print("Good morning")
    elif hour<18:
        print("Good afternoon")
    else:
        print("Good evening")
def welcome(f,l):
    greetuser()
    print(f"Welcome to the game, {f}{l}!")
    age=int(input("Enter your age: "))
    if(age>18):
        print("Eligibility statisfied!")
        num=7
        inp=int(input("Guess a Number(1-10): "))
        if(num==inp):
            print("Correct!")
        # else:
        #     print("wrong.Try again!")
    else:
        print("You can't play this game!")

f=input("Enter a first name: ")
l=input("Enter a last name: ")

welcome(f,l)  