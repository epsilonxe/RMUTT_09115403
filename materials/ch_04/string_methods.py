x = 'ABCDEFAABBB'
print(len(x))  # Function len()
print(x.count('AB'))  # Method count()

print('Find \'C\' in x -->', x.find('C'))
print('Find \'A\' in x -->', x.find('A'))
print('Find \'Z\' in x -->', x.find('Z'))
print('Find \'a\' in x -->', x.find('a'))
print('Find \'DEF\' in x -->', x.find('DEF'))

print('Show index of \'C\' in x -->', x.index('C') )
print('Show index of \'A\' in x -->', x.index('A') )
# print('Show index of \'Z\' in x -->', x.index('Z') )  # ValueError

print('Replace "A" to "Z" in x: ', x.replace('A', 'Z') )
print('Replace "A" to "Z" in x: ', x.replace('A', 'Z', 2) )
