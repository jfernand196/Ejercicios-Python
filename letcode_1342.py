# Given an integer num, return the number of steps to reduce it to zero.

# In one step, if the current number is even, you have to divide it by 2, otherwise, 
# you have to subtract 1 from it.

 

# Example 1:

# Input: num = 14
# Output: 6
# Explanation: 
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.}

num = 14
cont = 0
while True:
    if num == 0:
        break
    elif num % 2 == 0:
        num = num / 2
        cont +=1
    elif num % 2 == 1:
        num = num - 1
        cont +=1
print(cont)
