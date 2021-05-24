import  re
import  os

file_path=".//pattern_file.txt"

if(os.path.isfile(file_path)):
    file_handle=open(file_path,'r')
    for line in file_handle:
