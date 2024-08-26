#Using case in a string with methods
from pyexpat.errors import messages

name = "mansur abdulfataih"
print(name.title())
print(name.upper())
print(name.lower())

#Concatenating Strings
first_name = "joe"
last_name = "collins"
full_name = first_name + " " + last_name
print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)