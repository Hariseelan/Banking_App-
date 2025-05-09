import os  # Import os module to check for file existence

account = {}
users = {}
account_file = "account.txt"
login_file = "login.txt"
      
    

#---------------Load Account Details---------------
def load_account():
    
    try :
        with open("load_account.txt","r") as load_account_file :
            for line in load_account_file :
                parts = line.strip().split(",")
                if len(parts) >= 3 :
                    acc_no = parts[0]
                    name = parts[1]
                    balance = float(parts[2])
                    transaction = parts[3:] if len(parts) > 3 else []
                    account[acc_no]={
                                    "name" : name,
                                    "balance" : balance,
                                    "transaction" : transaction
                    }
                    #load_account_file.write(account[acc_no])
    except FileNotFoundError:
        pass #file does not exist yet

#---------------Save Account Detail---------------
def save_account():
    with open("save_account.txt","a") as save_account_file:
        for acc_no,data in account.items():
            line = f"{acc_no:^10}{data['name']:^15}{' | '.join(data["transaction"]):^20}\n"
            save_account_file.write(line)

#---------------Load Login Details---------------
def load_login():
    
       
    try:
        with open("load_login.txt","r") as load_login_file:
            #print(load_login_file.read())
            for line in load_login_file:
                username,password,role,acc_no = line.strip()
                users[username] = {"username" :username,"password":password,"role":role,"acc_no":acc_no}
                #print(load_login_file.read())
    except FileNotFoundError:
        pass
        

#---------------Save Login Details---------------
def save_login():
    #if not os.path.exists(login_file):
        with open("save_login.txt","a") as save_login_file:
            for username,data in users.items():
                line = (f"{username:^15}{data['password']:^15}{data['role']:^10}{data['acc_no']:^10}\n")
                save_login_file.write(line)

#---------------Register New Customer---------------
def register_customer():
    username = input('Enter the Username : ')
    if username in users:
        print("Username already exists.")
        return

    password = input('Enter Your Password : ')
    name = input('Enter Your name : ')

    while True:
        balance_input = (input('Enter initial balance : '))
        try: 
            balance = float(balance_input)
            if balance >= 0:
                break
            else:
                print("Please Enter the valid amount")
        except ValueError:
            print("Invalid input please enter the valid numeric")  

    acc_no = str(len(account)+1001)

    users[username] = {"password" : password,"role" : "customer","acc_no" : acc_no}
    account[acc_no] = {"name" : name,"balance":balance,"transaction":[f"Initial deposit:{balance}"]}
    print(f"Account created! Your account number is {acc_no}")

#---------------Admin Menu---------------
def admin_menu():
    while True:
        print("\n=== Admin Menu ===")
        print("1.View All Account Detail")
        print("2.Exit")
        choice = input("choose: ")
        if choice == "1" :
            for acc_no,data in account.items():
                print(f"{acc_no}-{data['name']}-balance:{data['balance']}")
        elif choice == "2" :
            break
        else:
            print("Invalid choice.Please try again......")


#---------------Customer menu---------------
def customer_menu(acc_no):
    while True:
        print("\n ---Customer Menu--- ")
        print("1 >>> Deposit")
        print("2 >>> withdraw")
        print("3 >>> check balance")
        print("4 >>> Transaction History")
        print("5 >>> Exit")
        choice = input("choose : ")
        if choice == '1':
            amount = float(input("Enter amount to deposit : "))
            if amount > 0:
                account[acc_no]["balance"]+=amount
                account[acc_no]["transaction"].append(f"Deposited : {amount}")
                print ("Deposit Successful.")
        elif choice == '2' :
            amount = float(input("Enter amount to withdraw : "))
            if 0 < amount <= account[acc_no]["balance"] :
                account[acc_no]["balance"]-= amount
                account[acc_no]["transaction"].append(f"withdraw : {amount}")
                print("withdraw Successful.")
            else:
                print("Insufficient balance...Please try again...")
        elif choice == '3' :
            print("balance : ",account[acc_no]["balance"])
        elif choice == '4' :
            print("Transaction : ")
            for t in account[acc_no]["transaction"]:
                print("-",t)
        elif choice == '5' :
            break
        else :
            print("Invalid Choose---please enter the valid choose===")
        
#---------------Login--------------- 
def login():
    attempts = 3        # Allow 3 attemptd to Login
    while attempts > 0 :
        username = input("Enter your username : ")
        password = input("Enter your password : ")
        
        if username in users and users[username]['password']==password:
            role = users[username]['role']
            acc_no = users[username]['acc_no']

            if role == "admin" : 
                admin_menu()
            else:
                customer_menu(acc_no)
            break
        else:
            attempts -= 1
            if attempts > 0 :
                print(f"Invalid Login --- please try again --- you have {attempts} attempts left.")
            else:
                print("Too many Invalid attempts. Please try again Later.")
                break



#---------------Menu---------------
def main():
    load_account()
    load_login()
    

    while True :
        print("\n ---Welcome to Bank System---")
        print("1) Login")
        print("2) Register as Customer")
        print("3) Exit")
        choice = input("Choose : ")
        if choice == '1' :
            login()     # Call login after loading the login data
        elif choice == '2' :
            register_customer()
        elif choice == '3' :
            save_account()
            save_login()
            print("Good bye guys have a nice day thankyou and come again")
            break
        else :
            print("Invalid Option please try again")

    login()
        
#---------------Run the program---------------

main()
