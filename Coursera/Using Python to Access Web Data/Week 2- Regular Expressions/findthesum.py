#Finding the sum of the Numbers in the text file regex_sum_344005.txt using Regular Expressions to extract the numbers
# I also decided to change this into a function(the original assignment doesn't ask for that)

import re

def Filesum(the_file):
    mysum = 0
    myf = open(the_file, 'r')
    for line in myf:
        nums = re.findall('[0-9]+', line)
        for number in nums:
            mysum += int(number)
    return mysum
my_file = "regex_sum_344005.txt"
finalsum = Filesum(my_file)
print(finalsum)


"""Change to list comprehension one day NOTE: If you do something like "nums = [re.findall('[0-9]+', line) for line in myf]" nums will
have empty lists in it like this "[]", so you have to get rid of that to use sum()... ALSO, I'm pretty sure there is a way to do this
in one line :D"""
