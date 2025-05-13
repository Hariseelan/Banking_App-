import os       #---------------------------------Import os module to check for file existence-----------------------------------------

# Initialize dictionaries to store account and user details
account = {}
users = {}

# Define file paths for account and login data
account_file = "account.txt"
login_file = "login.txt"
      
    

#---------------Load Account Details---------------

def load_account():   
    try :
        with open("load_account.txt","r") as file :                         # Open the account file for reading
            for line in file :
                parts = line.strip().split(",")
                        
                acc_no = parts[0]                                       # Account number
                name = parts[1]                                         # Account holder name
                balance = float(parts[2])                               # Account balance
                transaction = parts[3:] if len(parts) > 3 else []       # Transaction history
                account[acc_no]={
                                "name" : name,
                                "balance" : balance,
                                "transaction" : transaction
                }
                    
    except FileNotFoundError:
        pass #______________________________________________________________ file does not exist yet
    
    return account



#---------------Save Account Detail---------------

def save_account():
    with open("save_account.txt","a") as save_account_file:
        for acc_no,data in account.items():
            line = f"{acc_no:^10}{data['name']:^15}{' | '.join(data["transaction"]):^20}\n"                         # Write each user's details in a formatted line
            save_account_file.write(line)



#---------------Load Login Details---------------

def load_login():
    
       
    try:
        with open("load_login.txt","r") as load_login_file:
            for line in load_login_file:
                username,password,role,acc_no = line.strip()
                users[username] = {"username" :username,"password":password,"role":role,"acc_no":acc_no}            # Store user login details in the users dictionary
                #print(load_login_file.read())
    except FileNotFoundError:
        pass
        


#---------------Save Login Details---------------

def save_login():
    if not os.path.exists(login_file):
        with open("save_login.txt","a") as save_login_file:
            for username,data in users.items():
                line = (f"{username:^15}{data['password']:^15}{data['role']:^10}{data['acc_no']:^10}\n")               # Write each user's details in a formatted line
                save_login_file.write(line)



#---------------Register New Customer---------------

def register_customer():
    username = input('Enter the Username : ').strip()
    if username in users:
        print("Username already exists.")
        return                                          # Exit the function if username already exists

    password = input('Enter Your Password : ').strip()
    name = input('Enter Your name : ').strip()

    while True:
        balance_input = (input('Enter initial balance : '))
        try: 
            balance = float(balance_input)
            if balance >= 0:
                break
            else:
                print("Please Enter the valid amount")
        except ValueError:
            print("\n !!! Invalid input please enter the valid numeric !!!")  

    acc_no = str(len(account)+1001)                                                                                     # Generate a unique account number

    # Store the new customer in the `users` and `account` dictionaries
    users[username] = {"password" : password,"role" : "customer","acc_no" : acc_no}
    account[acc_no] = {"name" : name,"balance":balance,"transaction":[f"Initial deposit:{balance}"]}
    print(f"Account created! Your account number is {acc_no}")



#---------------Admin Menu---------------

def admin_menu(account):
    while True:
        print("\n=== Admin Menu ===")
        print("1.View All Account Detail")
        print("2.Exit")
        choice = input("\n Enter choose : ")
        if choice == "1" :
            if account :
                print("\n ---Account Details---")
                for acc_no,data in account.items():
                    print(f"{acc_no}-{data['name']}-balance:{data['balance']}")
        elif choice == "2" :
            break
        else:
            print("\n     !!!     Invalid choice.Please try again......     !!!     ")



#---------------Customer menu---------------

def customer_menu(acc_no):
    while True:
        print("""\n        
            ===================
            ---Customer Menu--- 
            ===================""")
        print("1 >>> Deposit")
        print("2 >>> withdraw")
        print("3 >>> check balance")
        print("4 >>> Transaction History")
        print("5 >>> Exit")
        choice = input("\n Enter choose : ")
        if choice == '1':
            amount = float(input("Enter amount to deposit : "))
            if amount > 0:                                                          # Ensure the deposit amount is positive                    
                account[acc_no]["balance"]+=amount                                  # Update balance
                account[acc_no]["transaction"].append(f"Deposited : {amount}")
                print ("\n >>>>>>>>>> Deposit Successful. <<<<<<<<<<")
        elif choice == '2' :
            amount = float(input("Enter amount to withdraw : "))
            if 0 < amount <= account[acc_no]["balance"] :
                account[acc_no]["balance"]-= amount
                account[acc_no]["transaction"].append(f"withdraw : {amount}")
                print("\n >>>>>>>>>> withdraw Successful. <<<<<<<<<<")
            else:
                print("\n  !!!!!Insufficient balance...Please try again... !!!!!")
        elif choice == '3' :
            print("balance : ",account[acc_no]["balance"])                          # Display current balance
        elif choice == '4' :
            print("Transaction : ")
            for t in account[acc_no]["transaction"]:
                print("-",t)                                                        # Display all transactions
        elif choice == '5' :
            break                                                                   # Exit the customer menu
        else :
            print("Invalid Choose---please enter the valid choose---")



#---------------Login--------------- 

def login(users):
    attempts = 3                                                                     # Allow 3 attemptd to Login
    while attempts > 0 :
        username = input("Enter your username : ").strip()
        password = input("Enter your password : ").strip()
        acc_no_input = int(input("Enter your Account Number : ").strip())
        
                
        if  (username in users and users[username]['password']==password and users[username]['acc_no']==acc_no_input) :
            
            role = users[username]['role']
            acc_no = users[username]['acc_no']

            '''print("""\n 
            *****************************
            *                           *
            *   Login successful !!!    *
            *                           *
            *****************************
                                       
              "welcome,have a nice day" 
                                       
            *****************************
            \n""")'''

            if role == "admin" :        
                admin_menu()                                                            # Call admin menu with account data
            else:
                customer_menu(acc_no)                                                   # Call customer menu with account number
            break
        else:
            attempts = attempts-1
            if attempts > 0 :
                print(f"Invalid Login --- please try again --- you have {attempts} attempts left.")
            '''else:
                print("""\n
                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                Too many Invalid attempts. Please try again Later.

                !!!!!!!!!!!1!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                \n""")'''
            break



#---------------Menu---------------

def main():
    
    load_account()              # Load account data at the start
    load_login()                # Load login data at the start

    while True :
        print("""\n 
        ----------------------------
        ----------------------------
        ---Welcome to Bank System---  
        ----------------------------
        ----------------------------
        \n""") 

        print("1) Admin")
        print("2) Login")
        print("3) Register as Customer")
        print("4) Exit")
        choice = input("\n Enter Choose : ")
        if choice == '1' :
            admin_menu(account)    
        elif choice == '2' :
            login(users)            # Call login after loading the login data
            load_account()
            load_login()
        elif choice == '3' :
            register_customer()     # Register a new customer
            save_account()          # Save account data after registration
            save_login()            # Save login data after registration
        elif choice == '4' :
            print("""\n 
            ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            o                                                         o
            o  Good bye guys have a nice day thankyou and come again  o
            o                                                         o
            ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            """)
            break                   # Exit the program
        else :
            print("!!! Invalid Option please try again !!!")

            login(users)

     
        
#---------------Run the program---------------

main()      
