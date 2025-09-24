import math
import os
import random
import re
import sys


# if __name__ == '__main__':
#     n = int(input().strip())

#     if n % 2 != 0:
#         print("Weird")

#     elif n % 2 == 0 and 2 <= n <= 5:
#         print("Not Weird")

#     elif n % 2 == 0 and 6 <= n <= 20:
#         print("Weird")

#     elif n % 2 == 0 and n > 20:
#         print("Not Weird")

#     else:
#         print("Error")


# Leap Year Challenge
def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True

    return leap


print(is_leap(1992))
