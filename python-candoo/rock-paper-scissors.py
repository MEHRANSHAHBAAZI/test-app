from random import random, choice

def main():
    counter_user = 0
    counter_computer = 0
    for i in range(3):
        list = ["rock", "paper", "scissors"]
        while True:
            try:
                user = input("enter 1.rock , 2.paper , 3.scissors : ")
                if user not in list:
                    raise ValueError("Invalid input")
                break
            except ValueError:
                print("Please enter a valid choice: rock, paper, or scissors.")
                continue
        var_choice = choice(list)
        print(var_choice)

        if user == var_choice:
            print("draw")
        elif ((user == "rock" and var_choice == "scissors") or (user == "paper" and var_choice == "rock") or (user == "scissors" and var_choice == "paper")):
            print("user win")
            counter_user += 1
        else:
            print("computer win")
            counter_computer += 1
            
    return (counter_user, counter_computer)

counter_user, counter_computer = main()
print(counter_user, counter_computer)
if counter_user > counter_computer:
    print ("user is the winner")
elif counter_user == counter_computer:
    print ("user and computer are draw")
else:
    print ("computer is winner")