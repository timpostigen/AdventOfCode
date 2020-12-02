
import csv

def productOfSumMatchingEntries(targetSum, expenses):
    # Optimization: sort then cutoff

    for i in range(len(expenses)):
        base_expense = expenses[i]

        for expense in expenses[i+1:]:
            expenseSum = base_expense + expense

            if expenseSum == targetSum:
                return base_expense * expense

def productOfTripleSumMatchingEntries(targetSum, expenses):
    pass

targetSum = 2020

# from Convert from CSV to array in Python - https://stackoverflow.com/a/37174260
expenses = []
expenses_file_name = 'day-1-input.txt'

with open(expenses_file_name) as expenses_file:
    expenses_lines = expenses_file.readlines()
    for line in expenses_lines:
            expenses.append(int(line))

print(productOfTripleSumMatchingEntries(targetSum, expenses))
