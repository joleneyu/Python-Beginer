from os import sep



expenses = []
num_expenses = int(input('Enter the number of your expenses:\n'))
for x in range(num_expenses):
    expenses.append(float(input("Enter an expense:\n")))
total = sum(expenses)
print("You spent $", total, " on your lunch this week.", sep="")
