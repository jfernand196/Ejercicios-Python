nums = [1,2,3]
pares = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if i < j:
            if nums[i] == nums[j]:
                pares +=1

print(pares)



    