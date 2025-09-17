"""
NAME: Convert number to reversed array of digits
DESCRIPTION: Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
KATA URL: https://www.codewars.com/kata/5583090cbe83f4fd8c000051

EXAMPLES:
35231 => [1,3,2,5,3]
0     => [0]
"""

def digitize(n):
    arr = []
    n = str(n)[::-1]
    for i in n:
       arr.append(int(i))
    return arr