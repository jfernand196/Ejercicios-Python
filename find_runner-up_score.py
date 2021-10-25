# Given the participants' score sheet for your University Sports Day, you are required to find 
# the runner-up score.
# You are given  scores. Store them in a list and find the score of the runner-up.

n = 5
arr = [2,3, 6, 6, 5]
a = max(arr)
c = arr.count(a)

print(arr)
print(a)
print(c)

for i in range(c):
    arr.remove(a)

print(max(arr))
        
    

