account = {}
users = {}
account_file = "account.txt"
Login_file = "login.txt"

#TESTING EDIT AND ADD COMMIT AND PUSH

#---------------Load Account Details---------------
def load_account():
    try :
        with open(account_file,"r") as file :
            for line in file :
                parts = line.strip()
                acc_no,name,balance = parts[0],parts[1],float(parts[2])
                transaction = parts[3:] if len(parts) > 3 else : account[acc_no]={"name" : transaction}
    except FileNotFoundError:
        pass #file does not exist yet

#---------------Save Account Detail---------------
def save_account():
    with open(account_file,"w") as file:
        for acc_no,data,in account.items():
            line = (f"{acc_no}|{data['name']}|{data['balance']}|"+"|",join(data["transation"]))+"\n"
            file.write(line)

#---------------Load Login Details---------------
def load_login():
    try:
        with open(Login_file,"r") as file:
            for line in file:
                username,password,role,acc_no = line.strip()
                users[username] = {"password":password,"role":role,"acc_no":acc_no}
    except FileNotFoundError:
        pass


#---------------Save Login Details---------------
def save_login():
    with open(login.file,"w") as file:
        for username,data in user.items():
            line = (f"{username}|{data['password']}|{data['role']}|{data['acc_no']}\n")
            file.write(line)

#---------------Register New Customer---------------
def register_customer():
    username = input('Enter the Username : ')
    if username in users:
        print("Username already exists.")
        return
    password = input('Enter Your Password : ')
    name = input('Enter Your name : ')
    balance = float(input('Enter initial balance : '))
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
        