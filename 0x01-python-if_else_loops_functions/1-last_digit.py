#!/urs/bin/python3
import random
number = random.randit(-1000, 1000)
if number >= 0:
1_digit = number % 10
else:
1_digit = number % -10
print("last digit of {} is {}.format(number,1_digit),end = ' ')
if 1_digit > 5:
print("and is greater than 5")
elif 1_digit == 0:
print("and is 0")
else:
print("and is less than 6 and not 0)
