a = int(input("Enter a number: "))

result = ""

for i in range(1, a + 1):
    odd_number = 2 * i - 1
    result += str(odd_number)
    if i < a:
        result += ", "

print(result)
