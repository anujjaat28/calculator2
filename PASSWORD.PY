import random
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digit = "1234567890"
special_chars = "@#&$*%"
all_chars = alphabet + digit + special_chars
password_len = int(input("Enter length of password: "))
print(password_len)
password = "".join(random.sample(all_chars,password_len))
print(password)