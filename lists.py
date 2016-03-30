"""
numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers, end='\n\n')

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

# 1
numbers[0] = 'ten'
print(numbers)

# 2
numbers[-1] = 1
print(numbers)

# 3
print(numbers[2:])

#4
print(9 in numbers)
"""


"""
incomes = []
months = int(input("How many months? "))

for month in range(1, months + 1):
    income = float(input("Enter income for {} month: $".format(str(month))))
    incomes.append(income)
print("\nIncome Report\n-----------------")

total = 0
for month in range(1, months + 1):
    income = incomes[month - 1]
    total += income
    print("Month {:2d} - Income: ${:10.2f} Total: ${:10.2f}".format(month,
income, total))
"""


"""
numbers = []
user_num = 5

for first in range(1, user_num + 1):
    number = int(input('Number: '))
#   number = int(input('Enter Number {}: '.format(first)))
    numbers.append(number)

first_num = numbers[0]
last_num = numbers[-1]
mini = min(numbers)
maxi = max(numbers)

from statistics import mean

avg = mean(numbers)

print('\nThe last number is: ', last_num)
print('The smallest number is: ', mini)
print('The largest number is: ', maxi)
print('The average of the numbers is: ', avg)
print('FINISH.')
"""


"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = str(input('Enter Name: '))

while name not in usernames:
    print('Access Denied')
    name = str(input('\nEnter Name: '))
print('Access Granted')
"""


picks = []
quick_picks = int(input('How many quick picks? '))

for nums in range()






