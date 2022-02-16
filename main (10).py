# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S" and add_pepperoni == "Y":
    add_pepperoni = 2
elif add_pepperoni == "Y" and size == "M":
    add_pepperoni = 3
elif add_pepperoni == "Y" and size == "L":
    add_pepperoni = 3
else:
    add_pepperoni = 0

if size == "S":
    size = 15
elif size == "M":
    size = 20
elif size == "L":
    size = 25

if extra_cheese == "Y":
    extra_cheese = 1
else:
    extra_cheese = 0

total = int(size) + int(add_pepperoni) + int(extra_cheese)
print(f"Your final bill is: ${total}.")
