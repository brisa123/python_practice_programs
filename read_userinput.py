import os
import sys


input_length=len(sys.argv)
print(input_length)

output_file= sys.argv[input_length-1]
output_file_handle=open(output_file,'w')

for i in range(1, input_length-1):
    input_file=open(sys.argv[i], 'r')
    input_file_content=input_file.read()
    print(i," times \n")
    output_file_handle.write(input_file_content)
    input_file.close()

output_file_handle.close()






