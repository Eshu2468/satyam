#local variable : variable which stores inside the

surendra = "Data analyst"
print(surendra)
print("surendra")

#fuction : predifined code to execute rep

def greet():
    name = "surendra"   #local variable
    print("Hello", name)
    global suma
    suma = "data engineer"
    print("hello", suma)
    print("hello", surendra)
greet()

print(suma)

