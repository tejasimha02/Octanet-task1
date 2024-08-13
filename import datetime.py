import datetime

# Initial account details
account_balance = 1000.0
pin_code = "1234"
transaction_history = []

# Function to check balance
def check_balance():
    print(f"\nYour current balance is: ${account_balance:.2f}")
    transaction_history.append(f"Balance inquiry: ${account_balance:.2f} on {datetime.datetime.now()}")

# Function to withdraw cash
def withdraw_cash():
    global account_balance
    amount = float(input("Enter the amount to withdraw: $"))
    
    if amount <= 0:
        print("Withdrawal amount must be positive.")
    elif amount > account_balance:
        print("Insufficient balance!")
    else:
        account_balance -= amount
        print(f"${amount:.2f} withdrawn successfully!")
        transaction_history.append(f"Withdrew ${amount:.2f} on {datetime.datetime.now()}")

# Function to deposit cash
def deposit_cash():
    global account_balance
    amount = float(input("Enter the amount to deposit: $"))
    
    if amount <= 0:
        print("Deposit amount must be positive.")
    else:
        account_balance += amount
        print(f"${amount:.2f} deposited successfully!")
        transaction_history.append(f"Deposited ${amount:.2f} on {datetime.datetime.now()}")

# Function to change PIN
def change_pin():
    global pin_code
    old_pin = input("Enter your current PIN: ")
    
    if old_pin == pin_code:
        new_pin = input("Enter your new PIN: ")
        confirm_pin = input("Confirm your new PIN: ")
        
        if new_pin == confirm_pin:
            pin_code = new_pin
            print("PIN changed successfully!")
            transaction_history.append(f"PIN changed on {datetime.datetime.now()}")
        else:
            print("PIN confirmation doesn't match.")
    else:
        print("Incorrect current PIN!")

# Function to show transaction history
def show_transaction_history():
    print("\nTransaction History:")
    if not transaction_history:
        print("No transactions yet.")
    else:
        for transaction in transaction_history:
            print(transaction)

# Main function to simulate ATM
def atm_simulation():
    print("Welcome to the ATM Machine!")
    
    for _ in range(3):  # Allow user 3 attempts to enter correct PIN
        entered_pin = input("Please enter your PIN: ")
        if entered_pin == pin_code:
            while True:
                print("\nATM Menu:")
                print("1. Balance Inquiry")
                print("2. Cash Withdrawal")
                print("3. Cash Deposit")
                print("4. Change PIN")
                print("5. Transaction History")
                print("6. Exit")
                
                choice = input("Select an option: ")
                
                if choice == "1":
                    check_balance()
                elif choice == "2":
                    withdraw_cash()
                elif choice == "3":
                    deposit_cash()
                elif choice == "4":
                    change_pin()
                elif choice == "5":
                    show_transaction_history()
                elif choice == "6":
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
            break
        else:
            print("Incorrect PIN. Please try again.")
    else:
        print("Too many incorrect attempts. Exiting.")

# Run the ATM simulation
if _name_ == "_main_":
    atm_simulation()
