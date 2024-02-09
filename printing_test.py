first = "\u2656"
second = "\u2659"
third = "\u2657"

print(first*6)
print(second*6)
print(third*6)


fruit1 = "apple"
fruit2 = "orange"
fruit3 = second
fruit_array = [fruit1,fruit2, fruit3]

joined_line = ""
for each_fruit in fruit_array:
    joined_line = joined_line +each_fruit + "\t"
    print(each_fruit)

print("joined line")
print(joined_line)

