file= open('heroes.txt')
# data= file.read()
# print(type(data))
# print('\n')
# print(data)
# print('\n')
# print(repr(data))
# print('\n')
# print('lower:', data.lower())
# print('\n')
# print('UPPER:',data.upper())
# print('\n')
# print('count:',data.count('a'))
# print('\n')
# print('Replace:',data.replace('Wonder Woman','Hulk'))
# print('\n')
# print('Find:',data.find('Hulk'))
# print('\n')
# data= data.replace('Wonder Woman','Hulk')
# heroes = data.split("\n")
# for hero in heroes:
#     print(hero)

# print('hero1=', file.readline().strip())
# print('hero2=', file.readline().strip())
# print('hero3=', file.readline().strip())

heroes = file.readlines()

for hero in heroes:
    print(hero.strip())

file.close()

# result: 'Batman\nSuperman\nSpider-Man\nIron Man\nWonder Woman' 