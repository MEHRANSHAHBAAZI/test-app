def add (n1 , n2):
    return n1 + n2

def divide (n1 , n2):
    return n1 / n2 

def multiply (n1 , n2 ):
    return n1 * n2 

def subtract (n1 , n2 ): 
    return n1 - n2 

operations = {
    "+" : add , 
    "/" : divide , 
    "*" : multiply ,
    "-" : subtract ,
}

def calculate ():
    should_continue = True
    num1 = float(input("enter first number:  "))

    while should_continue:
        for symbol in operations:
            print (symbol)
        operation_symbol = input ("pick an operation from the line above :  ")
        num2 = float(input("enter next number  "))
        answer = operations[operation_symbol](num1 , num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        choice = input (f"type 'y' to continue with {answer} , or type 'n' to start a new calculation:  ")
        if choice == "y":
            num1 = answer
        else:
            should_continue = False 
            print ("\n " * 15)
            calculate()

calculate ()
