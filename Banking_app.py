#_____________________________________________________________BANKING APP MODEL________________________________________________________________

#---------------ACCOUNT CREATION---------------

# LOGIN SYSTEM WITH MAX RETRY (3_TIME)
# USERNAME AND PASSWORD

correct_username = "user123"
correct_password = "pass123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("""\t\t           =======================\n \t\t              Login successful!\n\t\t           =======================
        *******************                      **************************  
        *******************Welcome to Our service**************************
        *******************                      **************************\n""")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f" Invalid credentials. {remaining} attempt(s) left.\n")

if attempts == max_attempts:
    print(""" Too many failed attempts. Exiting program.
    ---------------------PLEASE------------------------
    ----------------CONTACT OUR BANK-------------------
    --------------------THANKYOU----------------------- """)
    exit()


# MENU LOOP + THROUGH ACCOUNT BALANCES


account_balances = [0]            # EXAMPLE ACCOUNT BALANCE
selected_account = 0              # WE'RE WORKING WITH ACCOUNT DEFAULT

'''def account_balances():
    pass

def withdraw():
    pass

def deposit():
    pass

def show_details():
    pass'''


while True:
    print("1.Check Balance")
    print("2.Withdraw Money")
    print("3.Deposit Money")
    print("4.View All Account Balance") 
    print("5.Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print(f"Account {selected_account} Balance: ${account_balances[selected_account]}")

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= account_balances[selected_account]:
            account_balances[selected_account] -= amount
            print(f"Withdrawal successful. New balance: ${account_balances[selected_account]}")
        else:
            print("Insufficient funds!")

    elif choice == "3":
        deposit = float(input("Enter amount to deposit: $"))
        account_balances[selected_account] += deposit
        print(f"Deposit successful. New balance: ${account_balances[selected_account]}")

    elif choice == "4":
        print("\n All Account Balances:")
        for i, balance in enumerate(account_balances):
            print(f"Account {i + 1}: ${balance}")
        print()

    elif choice == "5":
        print("Thank you for using our bank. Goodbye!")
        break

    else:
        print("'SORRY' Invalid choice. Please select a number between 1 and 5.\n")

