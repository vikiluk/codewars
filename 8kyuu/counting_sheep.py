"""
NAME: Counting sheep...
DESCRIPTION: Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
KATA URL: https://www.codewars.com/kata/54edbc7200b811e956000556

EXAMPLES:
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
  
The correct answer would be 17.
"""

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count
        