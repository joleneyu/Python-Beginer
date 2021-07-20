total = 0
expenses = []
for x in range(1,7,1):
    expenses.append(float(input("Enter the expenses:\n")))
total = sum(expenses)
print("You spent $", total, " on your lunch this week", sep='')

