"""
NAME: Removing Elements
DESCRIPTION: Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
KATA URL: https://www.codewars.com/kata/5769b3802ae6f8e4890009d2

EXAMPLES:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
"""

def remove_every_other(my_list):
    return my_list[::2]