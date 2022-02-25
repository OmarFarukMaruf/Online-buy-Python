def password():
    i = 0
    while i < 3 :
        Pass = input("Enter Your Password: ")
        if Pass == "12345":
            print("Successfully Login!")
            break
        else:
            print("Your are getting wrong!")
        i+=1

    if i == 3:
        print("Too many Tries!")
        exit()
