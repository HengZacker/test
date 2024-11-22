import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678"

print("Hello welcome to our website!")

numbers = input("How many passwords to do you want us to generate?: ")
numbers = int(numbers)

length = input("How long do you want the password to be?: ")
length = int(length)

print("/nhere are your passwords: ")

for X in range(numbers):
  passwords = ""
  for Y in range(length):
    passwords += random.choice(chars)
  print(passwords)
