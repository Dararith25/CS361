'''
Name: Dararith Huy
Class: CS 361
Date: July 17, 2023
'''

# import library to used in the code 
import getpass
import random
import string



# function to register a new user 
def Register():
    # get the all the input from the user 
    username = input("Username: ")
    masterPassword = getpass.getpass("Master Password: ")
    confirmMasterPassword = getpass.getpass("Confirm Master Password: ")
    
    # confirm that the password and the confirm password is the same 
    while(masterPassword != confirmMasterPassword):
        print("The confirm password does not match! Please try again.")
        confirmMasterPassword = getpass.getpass("Confirm Master Password: ")
    
    # store the user information
    userData = {
        "username": username,
        "masterPassword": masterPassword
    }
    
    # open the file in 'append' mode
    with open('account.txt', 'a') as file:
        # write the user data to the file
        file.write(str(userData) + "\n")
    
    filename = username + ".txt"
    # create a blank file to store the password
    with open(filename, 'w') as file:
        pass
   

 
# function to read the user data from the database
def ReadUserData(filename):
    with open(filename, 'r') as file:
        # read the contents of the file
        contents = file.read()

        # convert the string to a dictionary
        userDataList = [eval(line) for line in contents.split('\n') if line.strip()]

        # return the list 
        return userDataList  
   
  
   
# function for the user to view their password 
def ViewPassword(filename):
    # call function to get a list of password 
    passwordList = ReadUserData(filename)
    
    # print the list of password to the user  
    for item in passwordList:
        print(f"   Application: {item['applicaionName']}")
        print(f"   Password: {item['password']}\n")



# function for the user to entere their own password
def EnterPassword(filename):
    # print the prompt to the user and take in the user input
    print("\nUser's Password\n")
    applicaionName = input("   Please enter the application name: ")
    password = getpass.getpass("   Please enter the password: ")
    
    # store and application name and the password
    passwordToSave = {
        "applicaionName": applicaionName,
        "password": password
    }
    
    # open the file in 'append' mode
    with open(filename, 'a') as file:
        # write the user data to the file
        file.write(str(passwordToSave) + "\n")
    
    
    
# function to generate a passord 
def GeneratePassword(filename):
    print("\nGenerate Password\n")
    applicaionName = input("   Please enter the application name: ")
    lengthOfPassword = input("   Please enter the length of the generated password: ")
    
    # define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # generate the password
    password = ''.join(random.choice(characters) for _ in range(int(lengthOfPassword)))
    
    # store and application name and the password
    passwordToSave = {
        "applicaionName": applicaionName,
        "password": password
    }
    
    # open the file in 'append' mode
    with open(filename, 'a') as file:
        # write the user data to the file
        file.write(str(passwordToSave) + "\n")



# function to add new password 
def AddNewPassword(filename):
    # print out the prompt to the user
    print("\nAdd New Password")  
    print("   1. Enter Password.") 
    print("   2. Generate Password.\n") 
    
    # take input from the user 
    userInput = input("Please enter your option: ")
    
    # call funcion based on the user input
    if(userInput == "1"):
        EnterPassword(filename)
    elif(userInput == "2"):
        GeneratePassword(filename)
    
    
    
# function to delete existing password 
def DeletePassword(filename):
    print("\nDelete Password")
    ViewPassword(filename)  
    appNameToDelete = input("Please enter the application to delete: ")
    
    # call function to get a list of password 
    passwordList = ReadUserData(filename)
    
    # print the list of password to the user  
    for item in passwordList:
        if(appNameToDelete != item["applicaionName"]):
            applicaionName = item["applicaionName"]
            password = item["password"]
            
            # store and application name and the password
            passwordToSave = {
                "applicaionName": applicaionName,
                "password": password
            }
            
            # open the file in 'append' mode
            with open(filename, 'w') as file:
                # write the user data to the file
                file.write(str(passwordToSave) + "\n")
            
            
            
# call the function based on the input from the user 
def WelcomePageOption(userInput, filename):
    if(userInput == "1"):
        print("\nList of Saved Password:")
        ViewPassword(filename)
    elif (userInput == "2"):
        AddNewPassword(filename)
    elif (userInput == "3"):
        DeletePassword(filename)



# function to show the user the welcome page
def WelcomePage(username):
    # print out the prompt to the user 
    print(f"\nWelcome {username}, ")
    print("   1. View Password.")
    print("   2. Add New Password.")
    print("   3. Delete Password.")
    print("   4. Exit\n")
    
    # take input from the user 
    userInput = input("Please enter your option: ") 
    
    # call fucntion for the user input
    WelcomePageOption(userInput, (username+".txt"))
    
    # loop until the user want to exit
    while(userInput != "4"):
        # print out the prompt to the user
        print(f"\nWelcome {username}, ")
        print("   1. View Password.")
        print("   2. Add New Password.")
        print("   3. Delete Password.")
        print("   4. Exit\n")
        
        # take input from the user
        userInput = input("Please enter your option: ") 
        
        # call fucntion for the user input
        WelcomePageOption(userInput, (username+".txt"))
    
    

# function to login the existing user 
def Login():
    # get the input from the user 
    username = input("Username: ")
    masterPassword = getpass.getpass("Master Password: ")
    
    # call fuction to get a list of registered user 
    userList = ReadUserData('account.txt')
    
    # loop to find the registered user 
    for userData in userList:
        if((username == userData["username"]) and 
           (masterPassword == userData["masterPassword"])):
            WelcomePage(username)
        
        # when the user enter an account that is not registered
        else:
            print("--------------------------------------")
            print("No user found!!!")
            print("Please register before signing in.")
            print("--------------------------------------")
            


# print the prompt to the user 
print("Password Manager")
print("   1. Register[For new user].")
print("   2. Login with existing account.\n")

# take the user input 
userInput = input("Please enter your option: ")

# call function based on the user input
if(userInput == "1"):
    Register()
elif(userInput == "2"):
    Login()