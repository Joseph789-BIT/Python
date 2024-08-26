motorcycles = ['suzuki', 'honda', 'yamaha']
print(motorcycles)

# This changes the value of the first item to 'toyota'.
motorcycles[0] = 'toyota'
print(motorcycles)

# Adds 'toyota' at the end of the list without affecting any of the other elements in the list.
motorcycles.append('toyota')
print(motorcycles)

# Inserts the value 'roller' at the beginning of the list,
motor_cycles = ['honda', 'suzuki', 'yamaha']
motor_cycles.insert(0, 'roller')
print(motor_cycles)


# Removing element from a list
motorcycles = ['honda', 'cortex', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# Removing an item using pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['gen', 'g-links', 'powerline', 'vespa']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# Removing an item by value
