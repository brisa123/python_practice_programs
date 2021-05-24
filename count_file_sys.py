
import os
import sys

print (len(sys.argv))
debug_mode=0
if (len(sys.argv) == 3):
    debug_mode=1

basepath= sys.argv[1]
#debug_mode= sys.argv[2]
file_list=os.listdir(basepath)
file_open=open("report.txt",'w')
counter=0
flag=0
for filename in file_list:
    #print(filename,"\n")
    print("\n")
    if os.path.isfile(os.path.join(basepath,filename )):

        if (debug_mode):
            print(filename,"is a file")

        file_open.write(filename  + " is a file \n")
        counter=counter+1

    elif(os.path.isdir(os.path.join(basepath,filename))):
        if (debug_mode):
            print(filename, "is directory")
        file_open.write(filename + " is directory \n")
        flag=flag+1

print(counter, "number of files")
print(flag , "number of directories" )

file_open.write(str(counter) + " number of file")
file_open.write(str(flag) + " number of directories")

print(sys.argv[0], "is the script name")
print(sys.argv[1] , "is the directory argument given")


