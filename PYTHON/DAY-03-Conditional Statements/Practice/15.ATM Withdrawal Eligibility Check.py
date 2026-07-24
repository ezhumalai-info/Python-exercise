balance = float(input("Enter Account Balance: "))
withdraw = float(input("Enter Withdrawal Amount: "))

if withdraw <= balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance")