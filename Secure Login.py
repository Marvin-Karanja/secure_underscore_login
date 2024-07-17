print("SECURE LOGIN")
username = input("Enter your username: ")
password = input("Enter your password: ")
while username and password:
    if username != "Marvin" or password != "Python":
        print("Incorrect credentials. Try Again")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username != "Marvin" or password != "Python":
            print("Incorrect credentials. Try Again")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username != "Marvin" or password != "Python":
                print("You tried three times. Please enter your security question")
                security_question = input("Enter your security question ")
                if security_question == "What is your favorite movie? ":
                    print("Welcome to the System")
                    break
                else:
                    print("You are locked out of the system") 
                    break          
    else:
        print("Welcome To the System")
        break 
    