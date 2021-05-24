import re
import sys
import  os

my_string = "treyfrTT34256tfrsert3425"

match=re.search(r'(\w[a-z|A-Z]+)(\d+)(\w+[a-z]+)(\d+)',my_string)
if(match):
    alpha=match.group(1)
    digits=match.group(2)
    alpha1=match.group(3)
    digits1=match.group(4)
    print(alpha)
    print(digits)
    print(alpha1)
    print(digits1)
    total_letters = len(alpha) + len(alpha1)
    print (total_letters)
