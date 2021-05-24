import os
#file=open("My_Notes", "C:\Arpita\Arpita Study")

#for filename in os.listdir(os.getcwd()):
 #   print(filename)
for eachfile in os.getcwd():
    if eachfile=="result.txt":
        del(eachfile)

file = open("result.txt", 'w')
for filename in os.listdir("C://Arpita//Arpita Study"):
    print(filename)
    file.write(filename + "\t" + "Hello" + "\n")




print(type(file))

file.close()
