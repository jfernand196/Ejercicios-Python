# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.

# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation: 
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.


x = [[1,5],[7,3],[3,5]]
mayor = [sum(x[e]) for e in range(len(x))]
print(max(mayor))




# solucion 1
# def maximumWealth(self, accounts: List[List[int]]) -> int:
#         return max([sum(accounts[e]) for e in range(len(accounts))])

# solucion 2
#  def maximumWealth(self, accounts: List[List[int]]) -> int:
#         suma = 0
#         mayor = []
#         for i in accounts:
#             suma = 0
#             for e in i:
#                 suma += e
#             mayor.append(suma)

#         return max(mayor)

