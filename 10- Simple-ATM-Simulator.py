#initially i will keep some amount in the bank.
balance = 10000  

while True:
    print("\n... ATM SIMULATOR ...")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

#i am taking the input of for the choice.
    choice = input("Enter choice: ")


    if choice == '1':
        print(f"Current Balance: ₹{balance:.2f}")

    # so here when the user tries to deposit the amount i ahve added the previous balance and the amount they wanted to deposite
    elif choice == '2':
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print(f"Updated Balance: ₹{balance:.2f}")
        else:
            print("Invalid deposit amount!")

    # when the user takes amount i have substracted it from the balance.
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("Invalid withdrawal amount!")

        elif amount > balance:
            print("Insufficient balance!")

        elif balance - amount < 500:
            print("Minimum balance of ₹500 must remain!")
        
        else:
            balance -= amount
            print("Withdrawal successful!")
            print(f"New Balance: ₹{balance:.2f}")

  
    elif choice == '4':
        print("Thank you for using ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1-4.")
