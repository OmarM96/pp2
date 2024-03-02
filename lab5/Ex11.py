import re
with open('/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS5/row.txt', 'r') as file:
    comp=file.read()
pettern=re.compile(r'([A-z]*[ ])')
result=pettern.sub(r'_', comp).lower()
print(result)