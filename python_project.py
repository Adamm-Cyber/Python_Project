# def say_hi(name):
#     print("Hello "+ name)

# say_hi("Adam")


# def say_hi(name , age):
#     print("Hello "+ name+  " your age is: " + str(age))

# say_hi("Adam" , 23)
#++++++++++++++++++++++++++++++++++++++++++

def cube(num):
     num*num*num

print(cube(3)) # we dont have anything to return a value from the function, so must be use > return as:

def cube(num):
    return num*num*num

print(cube(3)) 

#or

def cube(num):
    return num*num*num
# we able to store this function inside any variable as:
result = cube(4)
print(result)    


def add(num1 , num2):
    return num1 + num2

result = add(6,6)
print(result)
