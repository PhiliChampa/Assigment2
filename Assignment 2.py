# Question 1

print(" ")
print("Question 1:")
x = range(1, 11, 2)
for n in x:
    print(n)

# Question 2

print(" ")
print("Question 2:")
my_string = "Print even for every word in this sentence that has an even number of letters."

words = my_string.split()

new_strings = []

for string in words:
    if len(string) % 2 == 0:
        new_string = "even"
    else:
        new_string = string
    new_strings.append(new_string)


def join_string(list_string):
    string = ' '.join(list_string)

    return string

answer1 = join_string(new_strings)

print(answer1)

# Question 3

print(" ")
print("Question 3:")
strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
           "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37",
           "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55",
           "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73",
           "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91",
           "92", "93", "94", "95", "96", "97", "98", "99", "100", ]

new_strings = []

for string in strings:
    if int(string) % 3 == 0 and int(string) % 7 == 0:
        new_string = "FizzBuzz"
    elif int(string) % 7 == 0:
        new_string = "Buzz"
    elif int(string) % 3 == 0:
        new_string = "Fizz"
    else:
        new_string = string
    new_strings.append(new_string)

print(new_strings)

# Question 4

print(" ")
print("Question 4:")

num1 = 32
num2 = 20

num3 = 22
num4 = 31


def is_less(num1, num2):
    if num1 > num2:
        return True
    else:
        return False


answer4 = is_less(num1, num2)
print(answer4)

answer5 = is_less(num3, num4)
print(answer5)

# Question 5

print(" ")
print("Question 5:")

num_list = [4, 2, 5, 1, 3, 10]


def is_odd_list(num_list):
    return_list = []
    for num in num_list:
        if not (num % 2 == 0):
            return_list.append(num)
    return return_list


answer6 = is_odd_list(num_list)
print(answer6)
