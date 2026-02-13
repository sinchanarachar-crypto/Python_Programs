# Banking system using dictionary 
bank = {"account_number": 12345, "name": "John Doe", "balance": 1000} 
print("Welcome to Simple Bank System") 
print("Account Holder:", bank["name"]) 
print("Account Number:", bank["account_number"]) 
print("Current Balance:", bank["balance"]) 
while True: 
    print("\nChoose an option:") 
    print("1. Deposit") 
    print("2. Withdraw") 
    print("3. Check Balance") 
    print("4. Exit") 
    choice = input("Enter choice (1-4): ") 
    if choice == "1": 
        amount = int(input("Enter deposit amount: ")) 
        bank["balance"] += amount 
        print("Deposit successful! Updated Balance:", bank["balance"]) 
    elif choice == "2": 
        amount = int(input("Enter withdrawal amount: ")) 
        if amount <= bank["balance"]: 
            bank["balance"] -= amount 
            print("Withdrawal successful! Updated Balance:", bank["balance"]) 
        else: 
            print("Insufficient balance!") 
    elif choice == "3": 
        print("Current Balance:", bank["balance"]) 
    elif choice == "4": 
        print("Thank you for banking with us!") 
        break
    else: 
        print("Invalid choice, please try again.") 