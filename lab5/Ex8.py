import re

with open('/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS5/row.txt', 'r') as file:
    comp=file.read()
pattern=re.compile(r'([A-Z][a-z])*')
result=pattern.sub(r'', comp).upper()
print(result)