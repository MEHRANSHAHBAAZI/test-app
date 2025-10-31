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
c_u, c_p = main()
print(c_u , c_p)
if c_u > c_p:
    print ("user is the winner")
elif c_u == c_p :
    print ("user and computer are draw")
else:
    print ("computer is winner")