from openpyxl import Workbook

file = Workbook()
file1 = file.active
file1.title = "information"

file1["a1"] = "full name"
file1["b1"] = "phone number"
file1["c1"] = "email"
file1["d1"] = "address"

question = int(input("how many persons do you want to add?"))
for i in range(question):
    fullname = input("please enter your full name: ")
    phonenumber = int(input("please enter your phone number:"))
    email = input("please enter your email:")
    address = input("please enter your address:")   
    file1.append([fullname, phonenumber, email, address])
    file.save("information.xlsx")