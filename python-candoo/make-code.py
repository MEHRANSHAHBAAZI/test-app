import string
import random

letters = string.ascii_lowercase , string.ascii_uppercase
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!','#','$','%','&','*', '@']

print("Welcome to the Password Generator!")

user_name = input("Please enter your name: ")

user_letters = int(input("How many letters would you like in your password?\n"))
user_symbols = int(input(f"How many symbols would you like?\n"))   
user_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range (0, user_letters):
    password_list.append(random.choice(letters[0]))

for char in range (0, user_symbols):
    password_list.append(random.choice(symbols))

for char in range (0, user_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ""

for char in password_list:
    password += str(char)
    
print(f"Dear {user_numbers} your password is: {password}")
