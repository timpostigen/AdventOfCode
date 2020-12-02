def productOfSumMatchingEntries(targetSum, expenses):
    # Optimization: sort then cutoff

    for i in range(len(expenses)):
        base_expense = expenses[i]

        for expense in expenses[i+1:]:
            print(f"{base_expense}, {expense}")
            # if base_expense + expense == targetSum:
            #     return base_expense * expense


targetSum = 2020
expenses = [1721, 979, 366, 299, 675, 1456]

productOfSumMatchingEntries(targetSum, expenses)
