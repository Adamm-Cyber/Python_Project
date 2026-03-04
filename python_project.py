# is_hungry = True

# if is_hungry:
#     print("Go eat")

# else:
#     print("Do not eat")


# is_hungry = True
# wants_to_eat = True

# if is_hungry or wants_to_eat:
#     print("Go eat you are hungry or you just want to eat")

# else:
#     print("Do not eat")



is_hungry = False
wants_to_eat = True

if is_hungry and wants_to_eat:
    print("Go eat you are hungry or you just want to eat")

elif is_hungry and not wants_to_eat:
    print("eat so you can survive")

elif not is_hungry and wants_to_eat:
    print("Dont eat you are not hungry")
else:
    print("Do not eat")



