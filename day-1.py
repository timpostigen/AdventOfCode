
import csv

def productOfSumMatchingEntries(targetSum, expenses):
    # Optimization: sort then cutoff

    for i in range(len(expenses)):
        base_expense = expenses[i]

        for expense in expenses[i+1:]:
            expenseSum = base_expense + expense

            if expenseSum == targetSum:
                return base_expense * expense


targetSum = 2020

# from Convert from CSV to array in Python - https://stackoverflow.com/a/37174260
expenses = []
with open('day-1-input.txt') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
            expenses.append(row)

print(len(expenses))
print(productOfSumMatchingEntries(targetSum, expenses))
