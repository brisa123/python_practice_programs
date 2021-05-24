
import os

basepath="C://Arpita//Arpita Study"
file_list=os.listdir(basepath)
file_open=open("report.txt",'w')
counter=0
flag=0
for filename in file_list:
    #print(filename,"\n")    print("\n")
    if os.path.isfile(os.path.join(basepath,filename )):
        print("-------------------")
        print(filename,"is a file")
        file_open.write(filename  + " is a file \n")
        counter=counter+1

    elif(os.path.isdir(os.path.join(basepath,filename))):
        print(filename, "is directory")
        file_open.write(filename + " is directory \n")
        flag=flag+1

print(counter, "number of files")
print(flag , "number of directories" )

file_open.write(str(counter) + " number of file")
file_open.write(str(flag) + " number of directories")


