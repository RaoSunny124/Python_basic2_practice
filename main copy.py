# print("Hello World")
# print("two headalins")  
# print(2)
# Data types
# Primitive and non-primitive 


# #Primitive:u can store single value

# #str: string: anthing inside which come inside inverted commas is called string
# #int: integer: 1234241
# #float: decimal number:234.32434
# #bool: boolean: true\false
# print(type("lunch"))
# # ""
# # ''
# # """ """
# print("""'Quaid' said : "Work" Work and Work""")
# print('''Quaid said :
# Work Work and Work''')
# print('Quaid said : Work Work and Work')


# #Escape Sequence
# #\n : new line 
# #\t : tab space 
# #\\ : back slash
# print("Hassan \nAshraf")
# print("Hassan\tAshraf")
# print("Quaid said : \"Work\" Work and Work")

# #Variables
# name = 5.5
# print(name)
# #Rules
# #no space
# #father name = Ashraf
# #dont start with integer
# #2name = hassan
# #dont use special charactor
# #father&name = 'Ashraf'
# #dont use keyword
# #print = "Hassan"
# #print(print)
# #meaningful variable(it is for our help)

# #stages
# #declaration
# #initialization
# #name : int #dec
# #name = "Hassan" #init   


# #String
# #"Hassan"
# #indexing: always with[]
# #indexing
# #slicing
# #steping
# #Negative indexing
# nam : str = "My name is Hassan and I am a PIAIC student"
# print(nam[3])
# print(nam[0 : 17])
# print(nam[0 : 17 : 2])
# print(nam[:: -1])

# #immutable: anything which is unchangeable
# #mutable: anything which is changeable

# #String Function 
# #1. lower()
# #2. title()
# #3. capilization()
# #4. title
# #5. swapcase

# name2 = "Hassan Ashraf"
# second_str = name2.upper()
# print(name2.upper)#location
# print('this is original',name2)
# print('this is changed', second_str)
# second_str = name2.lower()
# print('this is original',name2)
# print('this is changed', second_str)
# second_str = name2.swapcase()
# print('this is original',name2)
# print('this is changed', second_str)
# second_str = name2.capitalize()
# print('this is original',name2)
# print('this is changed', second_str)
# second_str = name2.title()
# print('this is original',name2)
# print('this is changed', second_str)
# second_str = name2.center(50 , '_')
# print(name2)
# print( second_str)
# print(name2.endswith('raf'))
# print(name2.expandtabs(20))
# print(name2.find('a'))
# print(name2.index('s'))
# third_str = " ".join("Rao")
# print(third_str)
# print("Hassan", end = "_")
# print("Ashraf")


# #f_string
# age = 19
# print(f"My name is {name} and My age is {age}.")


# #using variable or without variable
# #num1 = 12
# #num2 = 2
# #print(num1 + num2)
# print(12 + 2)
# print(12 - 2)
# print(12 * 2)
# print(12 / 2)
# print(12 ** 2)
# print(12 % 2)
# print(12 // 2)

# #if\elif\else\nested statement
# i = 10
# if i > 15:
#     print("true")
# elif i != 10:
#     print("i am elif")
# else:
#     print('False')

# if i < 15:
#     print("true")
#     if i == 10:
#         print("nested")
#     else:
#         print("c false")    
# else:
#     print("P false")


# #loops


# #for loop
# #1.
# for x in range(1 , 11):
#     print(x)
# for x in range(1 , 11 , 2):
#     print(x)    
# for x in range(1 , 11):
#     print("Hassan")
# #2.
# My_name: str = ('Hassan')
# # for i in My_name:
# #     print(i)
# # for i in 'Hassan': #iterable = multiple values
# #     print(i)    
# # list1 = [2,2,4]
# # for i in list1:
# #     print(i)


# #while
# condition = True
# score = 0
# while condition:
#     print('Hello World')
#     score += 1
#     print(score)
#     user_input = input("Do u want to stop yes or no:")
#     if user_input == "yes":
#         condition = False


# count  = 0
# while count < 4:
#     print('Hello World')
#     count += 1


# #break
# count  = 0
# while count < 4:
#     print('Hello World')
#     break

# #nested for loop
# for x in range(1 , 10):
#     for y in range(10 , 20):
#         print(x , y)


# #Funtion
# #user_defined
# def even_odd(j):     # parameters(a , b):
#     if j % 2 == 0:
#         return 'even'          #no doubt print is used
#     else:
#         return 'odd'


# print(even_odd(4))   #Function calling + Arguments
# print(even_odd(int(input('number:'))))

# #default arguments
# # def even_odd(j = 5):     
# #     if j % 2 == 0:
# #         return 'even'          
# #     else:
# #         return 'odd'
# # print(even_odd(10))
# # print(even_odd(4))

# #conditional arguments
# def person_detail(first_name , father_name , age):
#     print(f"My name is {first_name} and my father name is {father_name} and my age is {age}.")

# person_detail('Hassan' , 'Ashraf' , 19)


# #keyword arguments
# # def person_detail(first_name , father_name , age):
# #     print(f"My name is {first_name} and my father name is {father_name} and my age is {age}.")

# # person_detail(first_name = 'Hassan' , age = 19 , father_name = 'Ashraf')


# # arbitary arguments
# def my_func(*argv):
#     for item in argv:
#         print(item)

# my_func(2 , 'Hassan' , 'Ali')        



# #keyword arbitary arguments
# def my_function(**kargv): 
#     """This function is about
#      keyword arguments"""
#     for key , value  in kargv.items():
#         print(f'{key} = {value}')


# my_function(my_age = 19 , me_name = 'Hassan' , papa_name = 'Ashraf')     


# #lamda
# add = lambda x, y : x+y
# print(add(5 , 2))


# #type casing
# naam = 'hasaan'
# li = list(naam)
# li[3] = 's'
# print(li)
# print(naam)
# str1 = "".join(li)
# print(str1)

