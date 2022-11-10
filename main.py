from openpyxl import Workbook, load_workbook
from student import Student
from openpyxl.utils import get_column_letter

wb = load_workbook('documents/košarka_evidencija.xlsx')
ws = wb.active
#print(ws['D3'].value)
#wb.save('documents/NovaEvidencija.xlsx')

col_range = ws['A:U']
row_range = ws[3:31]

studenti = []
for row in ws.iter_rows(3,35,None,None,True):
    for cell in row:
        if cell != None and cell != "+":
            osoba = Student(cell)
            studenti.append(osoba)

        if cell == "+":
            osoba.broj_dolazaka += 1

        if cell == None:
            osoba.broj_izostanaka += 1

for student in studenti:
    print(student.ime, "- Broj dolazaka:", student.broj_dolazaka,"- Ponasanje:",student.ponasanje())



