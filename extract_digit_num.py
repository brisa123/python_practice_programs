import re

my_str="My name is Arpita.. My roll No. is 25 , bharwadi  "

#match=re.search(r'.*is (\w[a-z|A-Z]+]).*is (\d+).*(\w[a-z]+).*',my_str)
match=re.search(r'.*is (\w[a-z]+).*(\d[0-9])+.*\s+(\w[a-z|A-Z]+)',my_str)
if(match):
    name = match.group(1)
    roll_no=match.group(2)
    place=match.group(3)
    print(name,roll_no,place)

