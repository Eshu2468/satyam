#string  methods
'''
Capitalize
Index

'''

s = "data analyst"
ashok = s.capitalize()
print(ashok)


#Index
text = "Hello world"
vishwa = text.index("world")
print(vishwa)

#count method
txt = "Hello world Hello"
satish = txt.count("Hello")
print(satish)

#center Method

a = "Hello world Hello"
b=a.center(30)
print(b)

#find method

a = "Hello world Hello"
b=a.find("world")
print(b)

#islower and lower method

a = "hello world hello"
b=a.islower()
print(b)

#Upper method

a = "HELLO WORLD HELLO"
b=a.isupper()
print(b)


#title
a = "hello world hello"
b=a.title()
print(b)


#isalpha method
a = "helloworldhello99"
b=a.isalpha()
print(b)


#isalphanumerical
a = "helloworldhello"
b=a.isalnum()
print(b)

#isdecimal

a = "4567"
b=a.isdecimal()
print(b)


#isascii
a = "4567"
b=a.isascii()
print(b)
