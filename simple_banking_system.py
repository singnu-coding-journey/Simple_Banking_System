print("Welcome to simple banking system.")
print("if you want to deposit money than type 'd'.")
print("if you want to withdraw money than type 'w'.")
print("if you want to check balance than type 'c'.")
print("if you want to quit than type 'q'.")


balance = 1000

while True:
    
    try:
        choice = input("Enter your choice: ").lower()
        
        if choice == 'd':
            deposit_amount = float(input("Enter your deposit amount: "))
            balance += deposit_amount
            print(f"your total amount is: {balance}")
        elif choice == 'w':
            withdraw_amount = float(input("Enter your withdraw amount: "))
            if withdraw_amount < balance:
                balance -= withdraw_amount
                print(f"your new balance: {balance}")
            else:
                print(f"sorry! you don't have {withdraw_amount} amount of money in your bank account.")
        elif choice == 'c':
            print(f"your current balance is: {balance} ")
        elif choice == 'q':
            print("Good bye!")
            break 
        else:
            print("Invalid choice please type 'd', 'w', 'c', or 'q' to quit.") 
    except ValueError:
        print("Invalid amount! please enter a number.")
        
                         


    
