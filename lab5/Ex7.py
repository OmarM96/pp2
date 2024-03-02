import re

with open('/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS5/row.txt', 'r') as file:
    comp=file.read()
pattern1=re.compile(r'[ ,.]+')
result=pattern1.sub(':', comp)
print(result)