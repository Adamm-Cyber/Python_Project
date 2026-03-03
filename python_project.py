# ""
# print ("Hello python")
# print("Hallo, ich bin Adam")
# #+++++++++++++++++++++++++++++++++++++++++++++
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")
# #+++++++++++++++++++++++++++++++++++++++++++++
# name = "Adam"
# age = "23"
# print("there was a boy called " + name)
# print("he was " + age + " years old")
# print("he liked his name " + name)
# name = "Hammam"
# age = "21"
# print("there was another boy called " + name)
# print("he was " + age + " years old")
# #+++++++++++++++++++++++++++++++++++++++++++++
# print("code\nzilla")
# text = "adam"
# print(text.lower())
# print(text.upper())
# print(text.upper().isupper())
# print(len(text))
# print(text[2])
# print(text.index("a"))
# text = "Codezilla"
# print(text.replace("Code" , "Mode"))
# #+++++++++++++++++++++++++++++++++++++++++++++
# print(2.444)
# print(3+5)
# print(3*3+1)
# print(3*(3+1))
# print(10%3)
# my_number = -5
# print(str(my_number) + " my favorite number")
# print(abs(my_number))
# print(pow(2,3))
# print(max(4,10))
# print(min(4,10))
# print(round(2.7))
# print(round(2.3))
# from math import *
# print(floor(2.7))
# print(ceil(3.1))
# print(sqrt(9))
# #+++++++++++++++++++++++++++++++++++++++++++++
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hallo " + name + " and your age is: " + age)
# ""
# #+++++++++++++++++++++++++++++++++++++++++++++

# num1 = input("Enter your first number: ")
# num2 = input("Enter your second number: ") 
# result = float(num1) + float(num2)
# print(result)
#+++++++++++++++++++++++++++++++++++++++++++++++

# friends = ["Adam" , 23 , True , False , ["Hammam" , 22]]
# print(friends[1])
#+++++++++++++++++++++++++++++++++++++++++++++++
# friends = ["Adam" , "Hammam" , "Rami" , "Ahmad" , "Saly"]
# print(friends[-1])
# print(friends[1:3]) #here i want index 2, so index 3 is not include (stop when you reach to the index 3)
# print(friends[0:5])
# print(friends[0:])
# print(friends[0:2])
# friends[0] = "Adam Mu"
# print(friends[0:])
#+++++++++++++++++++++++++++++++++++++++++++++++
#codezilla = ["Programming" , "python"  , "tutorial" , "css" , "HTML"]
# tutorila = ["extend" , "list1" , "codezilla"]
# codezilla.extend(tutorila)
# print(codezilla)
# codezilla.append("Javascript")
# print(codezilla)
# codezilla.insert(0,"Java")
# print(codezilla)
# codezilla.insert(2,"C#")
# print(codezilla)
# codezilla.remove("Programming")
# print(codezilla)
# codezilla.clear()
# print(codezilla)
# codezilla.pop() #remove the last index, and you can store this index inside the variable as:
# print(codezilla)
# what_was_popped = codezilla.pop()
# print(what_was_popped)
# print(codezilla.index("Programming"))
# print(codezilla.count("Programming"))# Number of Programming inside the list ex:
# codezilla_2 = ["css" , "css" , "css" , "html" , "Java"]
# print(codezilla_2.count("css"))
# codezilla.sort() #(ترتيب بالحروف)
# print(codezilla)

# Numbers = [30, 20, 67, 12, 32, 45, 67, 78]
# Numbers.sort()
# print(Numbers)

# list_new = codezilla.copy()
# print(list_new)


# codezilla.append(1)
# print(codezilla)
# print(list_new)
#+++++++++++++++++++++++++++++++++++++++++++++++
# codezilla = ["Programming" , "python"  , "tutorial" , "css" , "HTML"]
# list_new = codezilla
# print(list_new)
# codezilla.append(1)
# print(codezilla)
# print(list_new)
#+++++++++++++++++++++++++++++++++++++++++++++++
coordinates = (23,45) 
###coordinates[0] = 22 # Error (ممنوع تغير القيمة)
print(coordinates[1])

list_of_tuples = [(2,3), (4,5), (7,8)]
print(list_of_tuples)
list_of_tuples[0][0] = 33
print(list_of_tuples)
