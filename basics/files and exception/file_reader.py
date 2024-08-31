filename = 'pi_digit.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())