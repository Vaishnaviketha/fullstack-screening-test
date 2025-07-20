a = int(input("Enter a number: "))

count = a if a % 2 != 0 else a - 1

result = ""
i = 1

while i <= count:
    odd_number = 2 * i - 1
    result += str(odd_number)
    if i < count:
        result += ", "
    i += 1

print(result)
