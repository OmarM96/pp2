import re

with open('/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS5/row.txt', 'r') as file:
    comp=file.read()
pattern=re.compile(r'[A_Z][a-z]*')
result=pattern.findall(comp)
print(result)