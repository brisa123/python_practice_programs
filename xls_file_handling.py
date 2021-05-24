#read the fail test cases line from xls report and print the line

import  sys
import os
import xlrd

file_path= "C://Arpita//file_handling//data_file.xlsx"

file_handle=xlrd.open_workbook(file_path)
sheet=file_handle.sheet_by_index(0)

print(sheet)

sheet.cell_value(0,0)

#print no of rows and cols
print(sheet.nrows)
print(sheet.ncols)

#print col name
for i in range(sheet.ncols) :
    print(sheet.cell_value(0,i))







