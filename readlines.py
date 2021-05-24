#readlines from file and skip lines if not required.

import sys
import os

input_length= len(sys.argv)


output_file=(sys.argv[input_length-1])
output_file_handle=open(output_file,'w')

for i in range (1, input_length-1):
    input_file_handle=open(sys.argv[i], 'r')
    for line in input_file_handle:
        print(line)
        output_file_handle.write(line.strip() + "\t hello \n")
    input_file_handle.close()

output_file_handle.close()



