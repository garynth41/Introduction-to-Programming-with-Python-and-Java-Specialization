password = ""
while password != "secret":

    password = input("Please enter the password:")
    if password == "secret":
        print("Welcome!")
    else:
        print("Sorry, the password you entered is incorrect.  Please try again.")
        
