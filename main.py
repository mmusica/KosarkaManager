from openpyxl import Workbook, load_workbook
from student import Student
from openpyxl.utils import get_column_letter,get_column_interval, column_index_from_string

wb = load_workbook('documents/košarka_evidencija.xlsx')
ws = wb.active
#print(ws['D3'].value)


col_range = ws['A:U']
row_range = ws[3:31]

studenti = []
row_number = 3

for row in ws.iter_rows(3, 35, column_index_from_string('A'), column_index_from_string('H'), True):

    col_number = column_index_from_string('A')
    for cell in row:
        if cell != None and cell != "+" and cell!='-':
            osoba = Student(cell)
            studenti.append(osoba)

        if cell == "+":
            osoba.broj_dolazaka += 1

        if cell == None:
            ws.cell(row_number, col_number).value = "-"

        if cell == '-':
            osoba.broj_izostanaka += 1

        col_number += 1

    row_number += 1

for student in studenti:
    print(student.ime, "- Broj dolazaka:", student.broj_dolazaka,"- Ponasanje:", student.broj_izostanaka)

wb.save('documents/košarka_evidencija.xlsx')

