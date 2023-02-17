#Inputs from user

Loan = float(input("What is the initial size of your loan? "))
Interest =float(input("What is your monthly interest rate? ")) / 100
Payment = float(input("What is your monthly downpayment on the loan? "))

#Crash prevention

if (Loan * Interest) > Payment:
    print("You are too poor to pay off this loan you miserable fuck")
    exit(1)

#Calculation of loan

counter = 0
while (Loan * (1+Interest) - Payment) > 0:
    counter += 1
    Loan = Loan  * (1 + Interest) - Payment
    print(f"For month {str(counter)} the size of your loan is {Loan:.2f}")

print(f"You need to pay off your loan for {str(counter + 1)} months")
print(f"For month {str(counter + 1)} the remainder of your loan is {Loan:.2f}")




