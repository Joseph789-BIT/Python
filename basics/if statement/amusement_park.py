age = 14
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
 price = 10
else:
    price = 1
print("Your admission cost is $" + str(price) + ".")