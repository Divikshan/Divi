#-------Main_Manu--------

def Bank_info():
    while True:
        print("---Banking_System---")
        print("1.Create_account")
        print("2.Deposit_Money")
        print("3.Withdraw_Money")
        print("4.Check_Balance")
        print("5.Transation_History")
        print("6.Admin")
        print("7.Exit")
        Options = int(input("Chose_Your_Option 1,2,3,4,5,6,7: "))

#---------Calling_Functions------------

        if Options==1:
            print(Create_account())

        elif Options==2:
            print(Deposit())

        elif Options==3:
            print(Withdraw())

        elif Options==4:
            print(Check_Balance())

        elif Options==5:
            print(Transation_History())

        elif Options==6:
            print(Admin())
            
        elif Options==7:
            print(Exit())
            break

        else:
            print("Involude_Option_Try_Again")

#-----------Globals--------------


Next_account_number = 1001
accounts = {}
Admin_Username = "Divi_Harsha"
Admin_Password = "Divi2004"

#---------------------------------------Functions--------------------------------------------


#-----------Account--------------

def Create_account():
    global Next_account_number
    Name = input("Enter Name: ")
    Username = input("Enter Username: ")
    Password = input("Enter Password: ")

    try:
        initial_balnce=int(input("Enter_intial_balance_(>=0):"))
        if initial_balnce < 0:
            print("Initial_balance_cannot_be_negative.")
            return
    except ValueError:
        print("Please enter a valid number for the initial balance.")
        return  


    account_number = Next_account_number
    print (f"Your_account_number:{Next_account_number}")
    Next_account_number += 1

    accounts[account_number] = {
        'Name': Name,
        'Username': Username,
        'Password': Password,
        'Balance': initial_balnce,
        'Transaction_History': []
    }

    print(accounts)

    with open("customer.txt", "a") as file:
        file.write(f"{account_number},{Username},{Password},{initial_balnce}\n")
 
    print(f"Account created successfully for {Name}.")
    


#-----------Deposit--------------

def Deposit():
    try:
        account_number=int(input("Enter_Account_Number:"))

    except ValueError:
        print("Invalid_account_numbrer.")
        return


    #------'accounts'dictionary------
    
    account = accounts.get(account_number) 
    if not account:
        print("Account_not_found")
        return        
    
    try:
        amount = int(input("Enter amount to deposit: "))
    except ValueError:
        print("enter_a_valid_number.")
        return

    if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return
    

    account['Balance'] += amount
    account['Transaction_History'].append(f"Deposited: {amount}")

    print(f"Deposite: {amount}")
    print("Deposite_Successfull.")

    with open("customer.txt", "a") as file:
        file.write(f"{account_number},Deposit,{amount},{account['Balance']}\n")

    print(f"Your balance is: {account['Balance']}")






#-----------Withdraw--------------

def Withdraw():
    try:
        account_number=int(input("Enter_Account_Number:"))
    except ValueError:
        print("Invalid account number.")
        return

    #------'accounts'dictionary------

    account = accounts.get(account_number)   
    if not account:
        print("Account_not_found")
        return 

    try:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return
        if amount > account['Balance']:
            print(f"Insufficient funds. Your balance is {account['Balance']}.")
            return
    except ValueError:
        print("Invalid withdrawal amount entered. Please enter a valid number.")
        return


    account['Balance'] -= amount
    account['Transaction_History'].append(f"Withdrew: {amount}")
    
    print(f"Withdraw: {amount}")
    print("Withdraw_Successfull.")

    with open("customer.txt", "a") as file:
        file.write(f"{account_number},Withdraw,{amount},{account['Balance']}\n")


    print(f"Your balance is: {account['Balance']}")




#-----------Check_Balance--------------

def Check_Balance():
    try:
        account_number = int(input("Enter Account Number: "))
    except ValueError:
        print("Invalid account number.")
        return


    #------'accounts'dictionary------

    account = accounts.get(account_number)
    if not account:
        print("Account_not_found")
        return    
    
    print(f"Your current balance is: {account['Balance']}")

    with open("customer.txt", "a") as Check_Balancee:
        Check_Balance.write(f"{account_number},Check_Balance,{account['Balance']}\n")




#-----------Transation_History--------------

def Transation_History():
    try:
        account_number = int(input("Enter Account Number: "))
    except ValueError:
        print("Invalid account number.")
        return


    #------'accounts'dictionary------

    account = accounts.get(account_number)
    if not account:
        print("Account_not_found")
        return

    Trans = account.get('Transaction_History', [])

    if Trans:
        print("Transaction_History:")
        for transaction in Trans:
                print(transaction)
   
    else:
        print("No transaction history.")

    print(f"Your current balance is: {account['Balance']}")



#------------Admin------------

def Admin():
    Username = input("Enter_the_username:")
    Password = input("Enter_the_password:")

    if Username == Admin_Username and Password == Admin_Password:
        print("Login_Successful.")
        Admin_Options()

    else:
        print("Invalid_login.")


       
def Admin_Options():
    while True:
        print("\n---Admin_Options---")
        print("1.View_all_accounts.")
        print("2.Delete_an_account.")
        print("3.Exit.")

        Options = int(input("Chose_Your_Option 1,2,3:"))

        if Options == 1:
            View_All_Accounts()
        elif Options == 2:
            Delete_Account()
        elif Options == 3:
            Exit()
            break
        else:
            print("Invalid_Options.")


def View_All_Accounts():
    if not accounts:
        print("No_accounts")
        return

    print("\n---All_Accounts---")
    for account_number, details in accounts.items():
        print(f"Account Number: {account_number}")
        print(f"Name: {details['Name']}")
        print(f"Username: {details['Username']}")
        print(f"Balance: {details['Balance']}")
        print(f"Transaction History: {details['Transaction_History']}")
        print("--------------------")


def Delete_Account():

    try:
        account_number = int(input("Enter Account Number to Delete: "))
    except ValueError:
        print("Invalid account number.")
        return

    account = accounts.get(account_number)
    if not account:
        print("Account not found.")
        return

    del accounts[account_number]
    print(f"Account {account_number} has been deleted.")

    # Update the customer file (optional)
    with open("customer.txt", "w") as file:
        for account_number, details in accounts.items():
            file.write(f"{account_number},{details['Username']},{details['Password']},{details['Balance']}\n")




#-----------Exit--------------

def Exit():
    print("\nThank you for using our service!")
    print("Have a great day!")

Bank_info()


