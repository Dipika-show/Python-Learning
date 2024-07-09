#write a program to replace name and date
letter= '''Dear <|Name|>,
You are selected
<|Date|>'''

print(letter.replace("<|Name|>","Dipika").replace("<|Date|>","1st sep"))