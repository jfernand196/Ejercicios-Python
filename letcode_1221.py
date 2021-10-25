# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it in the maximum amount of balanced strings.

# Return the maximum amount of split balanced strings.

 

# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number
#  of 'L' and 'R'.
# Example 2:

# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number
#  of 'L' and 'R'.

s = "RLLLLRRRLR"
cont = 0
cont2= 0
output = 0

for i in s:
    if i == 'R':
        cont += 1
        if cont == cont2:
            output +=1
            cont2 = 0
            cont = 0
        
    elif i == 'L':
        cont2 += 1
        if cont == cont2:
            output +=1
            cont2 = 0
            cont = 0
        
    
print(output)

# solucion 2

# count = 0
# total = 0
# for i in s:
#     if i == 'L':
#         count += 1
#     else:
#         count -= 1
#     if count == 0:
#         total += 1
# print(total)

