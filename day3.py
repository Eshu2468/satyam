# '''
# Operators :

# 1. arithmetic Operators
# '''

# a=5
# b=10

# print(a+b)    #addition
# print(a-b) #substration
# print(a*b)  #multiplication
# print(a/b)    #division
# print(a//b)   #floor division
# print(a**b)   #expontiation
# print(a%b)   #modulus


# #comparision operator

# # ==  #equal to
# # !=  #not equal to
# # >   #greater than
# # >=   #greather than equal to
# # <  #lesser than
# # <=   #lesser than equal to


# x = 10
# y = 20

# print(x == y)
# print( x > y)
# print(x >= y)
# print(x != y)
# print(x <= y)
# print(x < y)


# #assignmnet operators

# +=
# -=
# /=
# *=
# //=
# **=
# %=

# m = 10

# m += 10
# print(m)

# m -= 2
# print(m)

# m *= 3
# print(m)

# m /= 4
# print(m)

# m //= 2
# print(m)

#logical operators

# and  - return true 
# or
# not


# a = 10
# b = 5


# print(a > 4 and a < 20)
# print(a > 70 or a > 30)
# print(not(a > 5))  #true


#slicing 


# name = "Kiran is a data analyst"

# print(name[0:6])
# print(name[:])
# print(name[4:30])
# print(name[0:])
# print(name[::2])
# print(name[::-1])

# numbers = [10,20,30, 40, 50, 60 ] 

# print(numbers[:])
# print(numbers[0:4])
# print(numbers[:8])
# print(numbers[::2])
# print(numbers[::-1])

# print(numbers[0:5:1])
# print(numbers[0:5:2])
# print(numbers[0:5:3])



# email = "deepu@gmail.com"
# domain = email[email.index("@")+1:]
# print(domain)


# email2 = "kirandataabalsyts@anz.com"
# domain2 = email2[email2.index("@")+1:]
# print(domain2)

# name = email2[:email2.index("@")]
# print(name)

# name2 = email[:email.index("@")]
# print(name2)



from datetime import datetime

input_date = "01-04-2025"
kiran = datetime.strptime(input_date, "%d-%m-%Y")

month_number = kiran.month
print(f"M{month_number}")


week_number = kiran.isocalendar()[1]
print(f"W{week_number}")
