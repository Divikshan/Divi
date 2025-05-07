#-------Main_Manu--------

def Bank_info():
    while True:
        print("---Banking_System---")
        print("1.Create_account")
        print("2.Deposit_Money")
        print("3.Withdraw_Money")
        print("4.Check_Balance")
        print("5.Transation_History")
        print("6.Exit")
        Options = int(input("Chose_Your_Option 1,2,3,4,5,6: "))

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
            print(Exit())
            break

        else:
            print("Involude_Optin_Try_Again")

#-----------Globals--------------


Next_account_number = 1001
accounts = {}

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

    account = accounts.get(account_number)
    if not account:
        print("Account_not_found")
        return

    with open("customer.txt", "a") as file:
        file.write(f"{account_number},{Username},{Password},{initial_balance}\n")
 
    print(f"Account created successfully for {Name}.")
    


#-----------Deposit--------------

def Deposit():
    account_number=int(input("Enter_Account_Number:"))

    account = accounts.get(account_number) 
    if not accounts:
        print("Account_not_found")
        return    

    amount = int(input("Enter amount to deposit: "))
    if amount > 0:
        account['Balance'] += amount
        print(f"Deposite: {amount}")
        print("Deposite_Successfull.")
    else:
        print("Enter a positive amount.")
    print(f"Your balance is: {account['Balance']}")


#-----------Withdraw--------------

def Withdraw():
    account_number=int(input("Enter_Account_Number:"))
    account = accounts.get(account_number)
    
    if not accounts:
        print("Account_not_found")
        return    
    
    amount = int(input("Enter amount to withdraw: "))
    if amount <= account['Balance']:
        account['Balance'] -= amount
        print(f"Withdraw: {amount}")
        print("Withdraw_Successfull.")
    else:
        print("Insufficient balance.")
    print(f"Your balance is: {account['Balance']}")



#-----------Check_Balance--------------

def Check_Balance():
    account_number=int(input("Enter_Account_Number:"))
    account = accounts.get(account_number)
    if not account:
        print("Account_not_found")
        return    
    
    print(f"Your current balance is: {account['Balance']}")



#-----------Transation_History--------------

def Transation_History():
    global balance
    account_number=int(input("Enter_Account_Number:"))
    account = accounts.get(account_number)

    if not account:
        print("Account_not_found")
        return
    
    if 'Transactions' in account and account['Transactions']:
        print("Transaction History:")
        for transaction in account['Transactions']:
            print(transaction)
    else:
        print("No transaction history available.")

    print(f"Your current balance is: {account['Balance']}")



#-----------Exit--------------

def Exit():
    print("\nThank you for using our service!")
    print("Have a great day!")

Bank_info()


