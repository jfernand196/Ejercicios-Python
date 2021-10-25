# Given an integer n and an integer start.

# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

# Return the bitwise XOR of all elements of nums.

 

# Example 1:

# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator.
# Example 2:

# Input: n = 4, start = 3
# Output: 8
# Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.

n = 4
start = 3

output = []
output1 = 0
for i in range(n):
    output.append(start + 2*i)
    output1 ^= output[i]
print(output1)


