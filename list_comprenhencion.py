# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # newlist = []
# # for x in fruits:
# #     if x != "banana":
# #         newlist.append(x)
    
# #     else:
# #         newlist.append("orange")
# # print(newlist)






# #newlist = [x for x in fruits if x != "banana"]
# #newlist = [x for x in fruits if x != "banana" else "orange"]
# #newlist = [x if x != "banana" if x != "cherry" else "orange" for x in fruits]
# newlist = [x for x in fruits if x != "banana" if x != "cherry" if x == "kiwi"]
# print(newlist)

# lst = []
# for i in range(100):
#     if i > 10:
#         for j in range(i):
#             if j < 20:
#                 lst.append(j)
# print(lst)

# [j for i in range(100) if i > 10 for j in range(i) if j < 20]


# def a(x):
#      return x
# a(2)

# b = lambda x: x
# b(2)

print((lambda x: x)(2))