# Get the loan details
money_owed = float(input("How much money do you owe, in aud?\n"))
annual_interest_rate = float(input("What is the annaual interest rate?\n"))
monthly_payment = float(input("How much is your monthly payment, in aud?\n"))
loan_months = int(input("How many months do you want to see results for?\n"))

# Divide annual interest rate to monthly interest rate and make it a percent
monthly_interest_rate = annual_interest_rate/100/12

for x in range(loan_months):
  # Add in interest
  monthly_interest = money_owed*monthly_interest_rate
  money_owed = money_owed + monthly_interest

  if (money_owed - monthly_payment < 0):
    print("You have paid off your loan in", x+1, "months.", "Last payment is", money_owed)
    break

  # Make payment
  money_owed = money_owed - monthly_payment

  # Print the results after this month
  print ("Paid", monthly_payment, "of which", monthly_interest, "was interest.", end=" ")
  print("Your loan is ", money_owed)