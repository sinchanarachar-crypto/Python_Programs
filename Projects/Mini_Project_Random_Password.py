import random
import string
pass_length=12
charvalues= string.ascii_letters + string.digits +string.punctuation
password=""
for i in range(pass_length):
    password+=random.choice(charvalues)

print("Your Random Password is: ",password)