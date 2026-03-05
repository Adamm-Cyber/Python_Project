# x = float(input("Enter your first number: "))
# y = float(input("Enter your second number: "))

# def cl(x,y):
#     return int(x) + int(y)
# result = cl(x,y)
# print(result)   

# def cl(x,y):
#     return int(x) * int(y)
# result = cl(x,y)
# print(result) 

# def cl(x,y):
#     return int(x) - int(y)
# result = cl(x,y)
# print(result) 

# def cl(x,y):
#     return int(x) / int(y)
# result = cl(x,y)
# print(result)

######OR####
x = float(input("Enter your first number: "))
operator = input("Enter the operator: ")
y = float(input("Enter your second number: "))

if operator == "+":
   print(x+y) 
elif operator == "-":
    print(x-y)  
elif operator == "*":
    print(x*y)        
elif operator == "/":
    print(x/y)
else: 
    print("Error, please try again!")
