import re

with open('/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS5/row.txt', 'r') as file:
    cont=file.read()
pattern1 = re.compile(r'ab*')
result1 = pattern1.findall(cont)
print(result1)