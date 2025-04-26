# # # #logical operators
# # # '''

# # # and
# # # or
# # # not

# # # '''

# # # a = 10
# # # b = 20

# # # print(a > 5 and b > 10)

# # # print(a < 5 and b < 10)

# # # print(a<5 or b > 10)

# # # print(not(a>5))

# # '''
# # Special operators are the two types of operators
# # 1. membership operators
# # 2. identity operators
# # '''

# # #below are the identity operators examples

a = [1,2,3,4,5]
b = [10,20,30,40,50]
c = a

print(a is c)
print(a is b)
print(a is not b)

# # #below are the membership operators

# # anjali = [10,20,30,40]
# # print(20 in anjali)
# # print(100 not in anjali)

# # #below are the examples of bitwise
# # '''
# # bitwise operator perform operations on binary
# # and(&) , or(|), xor(^), not(~), leftshift{<<}, rightshift(>>)
# # '''

# # a = 5  #0101
# # b = 3  #0011

# # print(a & b)
# # print(a | b)
# # print(a ^ b)
# # print(~a)
# # print(a << 1)  #a=0101 
# # print(a >> 1)


# #python conditional statements
# # 1. if else statement
# a = 10

# if a < 10:
#     print("a is greater than 10")
# else:
#     print("a is greater than 10")


# # 2. if - elif - else statements
# if a < 5:
#     print(" is less than 5")
# elif a == 10:
#     print("a equal to 10")
# else:
#     print("a is equal to somthing else")

# 3. nested if statements

a = 5

if a > 10:
    if a < 30:
        print("a is between 10 and 30")
    elif a == 30:
        print(" a is exactly 30")
    else:
        print("a is greater than 30")
else:
    print("a is 10 or less")

    

