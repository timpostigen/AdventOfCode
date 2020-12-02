
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


def productOfSumMatchingEntries(targetSum, expenses):
    # Optimization: sort then cutoff

    for i in range(expenses.__len__):
        base_expense = expenses[i]

        for expense in expenses[i:]:
            
            # if base_expense + expense == targetSum:
            #     return base_expense * expense


targetSum = 2020
expenses = [1721, 979, 366, 299, 675, 1456]
print(expenses)

# productOfSumMatchingEntries(targetSum, expenses)
