# 1.
x = 5
y = 10
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("Oooo needs some work") # Correct


# 2.
x = 5
y = 10
if len("Dog") < x:
    print("Question 2 works!") # Correct
else:
    print("Still missing out")


# 3. `
age = 18
if age > 18:
    print("You are of voting age!")
else:
    print("Argggggh! You think you can hoodwink me?! You're too young to vote!") # Correct


# 4.
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars") # Correct
else:
    print("Stick to lazy river")

# 5.
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26): # ** means exponential (2^3, 5^2)
    print("GOT QUESTION 5!") # Correct
else:
    print("Oh good you can count")
