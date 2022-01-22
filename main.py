"""
Given a list of size n as input. Give sum of all numbers from this list that are multiples of 5.
Input-> [10,5,3,4,25,6]
Output-> 40
"""

ls = [10,5,3,4,25,6]
ln = len(ls)
sum = 0
for i in range(0,ln):
  e = ls[i]
  if (e%5==0):
    sum = sum + e
print(sum)
