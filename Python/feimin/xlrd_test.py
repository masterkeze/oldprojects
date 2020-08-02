# read and write excel file
from xlrd import open_workbook

wb = open_workbook('input.xlsx')
sheet0 = wb.sheet_by_index(0)
for s in wb.sheets():
    print('Sheets:',s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(str(s.cell(row,col).value))
        print(', '.join(values))
    print()
