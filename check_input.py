import sys
import os

input_file_length=len(sys.argv)

output_file_path=sys.argv[input_file_length-1]

output_file_handle=open(output_file_path,'w')

for input_file in range(1, input_file_length-1):
    if(os.path.isfile(sys.argv[input_file])):
        input_handle=open(sys.argv[input_file],'r')
        for each_line in input_handle:
            output_file_handle.write(each_line.strip() + " hello \n")
        input_handle.close()
    else:
        print(sys.argv[input_file] , "is not a file type")

output_file_handle.close()