print("Welcome to the FizzBuzz Game!")

var_name = input("Please enter your name: ")
print(f"Hello, {var_name}! Let's start the game.")

var_range = int(input("Enter the range up to which you want to play FizzBuzz (maximum = 100): "))

for number in range(var_range + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

print("Thanks for playing the FizzBuzz Game!")