# Given two arrays of integers nums and index. Your task is to create target array under 
# the following rules:

# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in 
# target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.

# It is guaranteed that the insertion operations will be valid.

 

# Example 1:

# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# Explanation:
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
# 4            1        [0,4,1,3,2]

## EJEMPLO DE INSERTAR EN LISTAS
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
output = []

for i in range(len(nums)):
    output.insert(index[i], nums[i])
print(output)


## solucion 2

# for num, index1 in zip(nums, index):
#     output.insert(index1, num)
# print(output)