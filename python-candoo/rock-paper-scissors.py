from random import random, choice

def main():
    counter_user = 0
    counter_computer = 0
    for i in range(3):
        var_user = input("enter rock , paper , scissors: ")
        list = ["rock", "paper", "scissors"]
        var_choice = choice(list)
        print(var_choice)

        if var_user == var_choice:
            print("draw")
        elif ((var_user == "rock" and var_choice == "scissors") or (var_user == "paper" and var_choice == "rock") or (var_user == "scissors" and var_choice == "paper")):
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