import datetime
def greetuser():
    current_time=datetime.time
    hour=current_time.hour
    # if hour<12:
    #     print("Good morning")
    # elif hour<18:
    #     print("Good afternoon")
    # else:
    #     print("Good evening")
def welcome(f,l):
    print(f"Welcome to the game, {f}{l}!")

f=input("Enter a first name: ")
l=input("Enter a last name: ")
greetuser()
welcome(f,l)  