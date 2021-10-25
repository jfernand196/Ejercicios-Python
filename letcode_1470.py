# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Example 2:

# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]

nums = [1,2,3,4,4,3,2,1]
n = 4

x = [nums[x] for x in range(n)]
y = [nums[i] for i in range(n,n*2)]
z = []
for i in range(n): z.append(x[i]),z.append(y[i])
print(z)
