import os
import re

file_path=".//pattern_file.txt"
testnames=[]
if(os.path.isfile(file_path)):
    file_handle=open(file_path,'r')
    for line in file_handle:
        flag=0
        if(re.search(r'=.*'), line):
            flag=flag+1
        if(re.search(r'test name.*'), line):
            match=re.search(r'test name.*\s(\w[a-z|A-Z]+).*',line)
            if(match):
                testname=match.group(1)
                print(testname)
                testnames.append(testname)

    file_handle.close()
print(testnames)
print(flag)