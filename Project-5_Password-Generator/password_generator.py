# Project 5

# Easy Level - Order not randomised:
# e.g. 4 letters, 2 symbols, 2 numbers = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letters, 2 symbols, 2 numbers = g^2jk8&P


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

num_letters = int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# Easy first:

password = ""

###  for char in range(1, num_letters + 1):  
###      random_char = random.choice(letters)  
###      password += random_char  

# can simplify code above by not using the "random_char" intermediary, such as:

for char in range(1, num_letters + 1):
    password += random.choice(letters)

for char in range(1, num_numbers + 1):
    password += random.choice(symbols)

for char in range(1, num_symbols + 1):
    password += random.choice(numbers)

print(password)


# Hard version next:

new_password = ""

