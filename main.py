import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


random_list_of_letters = []
random_list_of_symbols = []
random_list_of_numbers = []

random_letters = ""
random_symbols = ""
random_numbers = ""

for i in range (0, nr_letters):
  n = random.randint(0, len(letters) - 1)
  i = letters[n]
  random_list_of_letters.append(i)

for letter in random_list_of_letters:
  random_letters += letter

for i in range (0, nr_symbols):
  n = random.randint(0, len(symbols) - 1)
  i = symbols[n]
  random_list_of_symbols.append(i)

for symbol in random_list_of_symbols:
  random_symbols += symbol

for i in range (0, nr_numbers):
  n = random.randint(0, len(numbers) - 1)
  i = numbers[n]
  random_list_of_numbers.append(i)

for number in random_list_of_numbers:
  random_numbers += number

password = random_letters + random_symbols + random_numbers
shuffled_password = ''.join(random.sample(password,len(password)))

print(f"Here is your password: {shuffled_password}")