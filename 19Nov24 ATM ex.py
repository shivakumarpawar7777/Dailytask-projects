balance = 10000  

while True: 
    print("ATM Menu: ")  
    print("1. Check Balance ") 
    print("2. Withdraw ") 
    print("3. Deposit ") 
    print("4. Exit ") 
    option = int(input("Enter your choice: ")) 
    if option == 1: 
        check = input("Enter your pin: ") 
        print("Your current balance is: ₹{balance}") 
        print("Have a nice day to you") 
    elif option == 2: 
        withdrawl = float(input("Enter amount to withdraw (in rupees): ")) 
        if withdrawl > balance: 
            print("Insufficient balance. Please try again.") 
        elif withdrawl <= 0: 
            print("Invalid amount. Please enter a positive value.") 
        else: 
            balance -= withdrawl 
            print(f"Withdrawal successful. Your new balance is: ₹{balance}") 
            print("Have a nice day to you") 
    elif option == 3: 
        pay_in = float(input("Enter amount to deposit (in rupees): ")) 
        balance += pay_in 
        print(f"Deposit successful. Your new balance is: ₹{balance}") 
        print("Have a nice day to you") 
    elif option == 4: 
        print("Thank you for using the ATM. Your card is being ejected...") 
        break 
    else: 
        print("Invalid option. Please try again.")