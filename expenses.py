from os import sep


expenses = [10.50, 15, 20.80, 17.50, 12, 5, 37]
sum = 0
for expense in expenses:
    sum = sum + expense
print(sum)

print("You spend $", sum, " on lunch this week.", sep='')

dinner  = [1, 2, 5, 8, 9, 11, 22]
total = sum(dinner)
print("You spend $", total, " on dinner this week.", sep='')