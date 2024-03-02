import re

with open('/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS5/row.txt', 'r') as file:
    comp=file.read()
pattern1=re.compile(r'ab{2,3}')
result=pattern1.findall(comp)
print(result)