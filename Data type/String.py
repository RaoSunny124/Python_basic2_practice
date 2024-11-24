name : str = 'Hassan'
print(name)
print(type(name))

father_name = "Ashraf"
print(father_name)
print(type(father_name))

intro = """My name is Hassan.
I am a student of PIAIC in Batch 62."""
print(intro)
print(type(intro))

intro1 = '''My name is Hassan.
I am a student of PIAIC in Batch 62.'''
print(intro1)
print(type(intro1))

intro2 = "I am Hassan. I'm 19 year old."
print(intro2)

quotes = """Quaid's said : "work , work and work" """
print(quotes)
print(type(quotes))

print(quotes.index)

print(quotes.upper())
print(father_name.upper())
print(name.upper())
print(intro.upper())


print(quotes.lower())
print(name.lower())
print(intro.lower())
print(father_name.lower())



print(quotes.title())
print(intro2.title())
print(name.title())
print(father_name.title())
print(intro.title())
name1 = 'HAssan ASHraf'
print(name1.title())


print(name1.swapcase())
print(quotes.swapcase())#reverse system
print(intro.swapcase())
print(intro1.swapcase())
print(name.swapcase())


print(intro.capitalize())
print(name1.capitalize())
print(intro2.capitalize())
print(quotes.capitalize())


print(name.center(50 , '_'))
print(quotes.center(100 , '@'))
print(father_name.center(50 , '$'))

print(father_name.endswith('Liaqat'))
print(quotes.endswith('rk" '))
print(name.endswith('san'))

print(name1.expandtabs(10))

print(intro2.find('9'))
print(intro.find('n'))

print(intro.index('n'))
print(intro2.index('9'))#because indexing start with 0

print(name.join('Rao'))
print('Ashraf'.join('Hassan'))

special_charactor = '$@#&^!'
var_type = special_charactor
print(type(var_type))

number_string = '123445'
print(type(number_string))

print(name , end = ' goodbye!')


