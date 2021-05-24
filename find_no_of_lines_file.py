#find no of lines in all files given by user

import os
import sys

input_file = sys.argv[1]
count=0
if(os.path.isfile(input_file)):
    file_handle=open(input_file,'r')
    for each_line in file_handle:
        count=count+1
        #print(each_line)
    print(count)
    file_handle.close()

else:
    print("file does not exist")



