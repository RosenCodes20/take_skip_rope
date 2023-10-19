string = input()
numbers_digit = []
take_list = []
skip_list = []
letter = ""
result = ""
for strings in string:
    if strings.isdigit():
        numbers_digit.append(int(strings))
    else:
        letter += strings

for index in range(len(numbers_digit)):
    if index % 2 == 0:
        take_list.append(int(numbers_digit[index]))
    else:
        skip_list.append(int(numbers_digit[index]))

for x, y in zip(take_list, skip_list):
    if x == 0:
        letter = letter[y:]
    elif x != 0:
        result = result + letter[:x]
        letter = letter[x + y:]

print(result)
