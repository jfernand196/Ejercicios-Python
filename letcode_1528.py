# Given a string s and an integer array indices of the same length.

# The string s will be shuffled such that the character at the ith position moves to indices[i] in 
# the shuffled string.

# Return the shuffled string.
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
# Example 2:

# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.

# You can create an auxiliary string t of length n.
# Assign t[indexes[i]] to s[i] for each i from 0 to n-1


s = "aiohn" 
indices = [3,1,4,2,0]
CADENAINDICES = list(indices)
g = 0
for f in indices:
        CADENAINDICES[f] = s[g]
        g +=1
SALIDA = "".join(CADENAINDICES)
print(SALIDA)

#def restoreString(self, s: str, indices: List[int]) -> str:
"""s = "aaiougrt" 
indices = [4,0,2,6,7,3,1,5]

splittedString = list(s)
newString = list(range(0,len(indices)))
counter = 0
for ind in indices:            
    newString[ind]=s[counter]
    counter += 1
CADENA = "".join(newString)
print(CADENA)"""







        
