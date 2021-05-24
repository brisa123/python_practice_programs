

my_string="Python is a programing lang. Python is interpreted."

unique_list=[]
duplicate_list=[]
sting_list=my_string.split()

print(sting_list)

for item in sting_list:
    if item in unique_list:
        duplicate_list.append(item)
    else:
        unique_list.append(item)

print(unique_list)
print(duplicate_list)