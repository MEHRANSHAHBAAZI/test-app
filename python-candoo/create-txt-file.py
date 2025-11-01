from webbrowser import open_new
for i in range (3):
    var_name = input("enter your name:")
    var_lastname = input("enter your last name:")
    var_id = int(input("enter your id:"))
    with open("data.txt", "a")as file:
        file.write(f"you are {var_name} {var_lastname} and this is your ID: {var_id}\n")