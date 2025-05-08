from banking_system import Create_account, Deposit, Withdraw, Check_Balance, Transation_History, Exit, Bank_info

if __name__ == "__main__":
    Bank_info()  # This will call the main menu loop



if 'Transactions' in account and account['Transactions']:
        print("Transaction History:")
        for transaction in account['Transactions']:
            print(transaction)