import re

with open('/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS5/row.txt', 'rb') as f:
    response = f.read().decode('utf-8')
pattern = r'\S*аб{0,}\S*|\S*ab{0,}\S*'#\w{0,}аб{0,}\w{0,}|\w{0,}ab{0,}\w{0,}
l = re.findall(pattern, response)
print(l)