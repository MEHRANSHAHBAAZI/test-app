from webbrowser import open_new
for i in range (3):
    name = input("enter your name:")
    lastname = input("enter your last name:")
    id = int(input("enter your id:"))
    with open("data.txt", "a")as file:
        file.write(f"you are {name} {lastname} and this is your ID: {id}\n")