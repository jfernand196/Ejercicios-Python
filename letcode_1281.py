# Given an integer number n, return the difference between the product of its digits and the sum of
#  its digits.
 

# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

n = 234
mul = 1
suma = 0
x = [int(i) for i in str(n)]
for i in x: mul *= i; suma += i
print(mul - suma)



