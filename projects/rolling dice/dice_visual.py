import pygal

from die import Die

die_1 = Die()
die_2 = Die()

result = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    result.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = result.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Result of rolling two D6 dice 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add()