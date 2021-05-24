#read a file and then print that file content to another file

import sys
import os


input_file=sys.argv[1]
output_file_path=sys.argv[2]

input_file_handle=open(input_file,'r')
input_file_content=input_file_handle.read()

output_file_handle=open(output_file_path,'w')
output_file_handle.write(input_file_content)


input_file_handle.close()
output_file_handle.close()




