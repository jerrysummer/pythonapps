correct_password  = "123"
name = input("Enter name: ")
password = input("Enter pwd")

while correct_password != password:
    password = input("Enter pwd again:")


print("Hi %s you are Logged in" % name)

