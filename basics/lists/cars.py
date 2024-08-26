#Sorting a list temporarily with the sorted() function
# You can also sort in reverse alphabetical order
cars = ['benz', 'high-lander', 'rolls royce', 'toyota']
cars.sort(reverse=True)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)