numbers = [1,2,3,4,6] # [2, 1, 4, 2, 3]
output = []
# for i in numbers:
#     if i % 2 == 0:
#         output.append(i/2)
#     else:
#         output.append(i + 1)

# print(output)

def parimp(x):
    # for i in x:
    #   if i % 2 == 0:
    #     output.append(int(i/2))
    #   else:
    #     output.append(i + 1)
    # return output
    return [int(i/2) if i%2 == 0 else int(i+1) for i in x]

print(parimp(numbers))

# [f(x) if condition else g(x) for x in sequence]


