my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_numbers = []

for number in  my_list:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("The list with unique elements only:")
print(unique_numbers)
