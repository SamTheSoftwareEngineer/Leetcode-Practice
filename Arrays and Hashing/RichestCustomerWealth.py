"""You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth."""


# Approach:
# Loop through the array and add the sum of wealth for each person
# If the totalWealth on any one person is greater than the maxWealth, return the totalWealth
def RichestCustomerWealth(accounts):
    maxWealth = 0

    for i in range(len(accounts)):
        totalWealth = sum(accounts[i])

        maxWealth = max(maxWealth, totalWealth)

    return maxWealth
