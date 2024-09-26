#Password Generator Project

import csv
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password(nr_letters, nr_symbols, nr_numbers):
    password = []
    for i in range(nr_letters):
        password.append(random.choice(letters))
    for i in range(nr_symbols):
        password.insert(random.randint(0,len(password)),random.choice(symbols))
    for i in range(nr_numbers):
        password.insert(random.randint(0,len(password)),random.choice(numbers))
    return ''.join(password)

def save_to_file(password,website_name):
    with open('passwords.csv', 'a') as myfile:
        # writer = csv.writer(myfile, delimiter =',')
        myfile.write(",".join([password,website_name]))
        myfile.write("\n")
    print("saved!")


def main():
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    generated = generate_password(nr_letters, nr_symbols, nr_numbers)
    website_name = input(f"What is website name?\n")
    save_to_file(generated, website_name)
    print(generated)

if __name__ == "__main__":
    main()