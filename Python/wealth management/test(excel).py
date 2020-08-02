#read and modify .xlsx file
import xlrd
data = xlrd.open_workbook('300416.xlsx')
table = data.sheets()[0]
nrows = table.nrows
for i in range(nrows):
    print(table.row_values(i))
