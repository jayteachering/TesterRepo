print("Enter a username:")

username = input("> ")

if(username == "Jay"):
    print(f"Welcome, {username}!")
    print("Enter a password:")
    password = input("> ")
    if(password == "67"):
        print("Login successful")
    else:
        print("Login unsuccessful")
else:
    print("Unauthorised access!")




