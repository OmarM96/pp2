import re
with open('/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS5/row.txt', 'r') as file:
    comp=file.read()
pattern=re.compile(r'([A-Z]*)')
result=pattern.sub(' \1', comp)
print(result)