num = (list(map(int, input("Enter the numbers: ").split())))
unique_numbers = []
for i in num:
    if i not in unique_numbers:
        unique_numbers.append(i)
print("List of unique numbers are:", unique_numbers)