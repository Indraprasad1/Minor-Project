import random
import string

pass_len = 6
charValue= string.ascii_letters + string.digits + string.punctuation

password=""
for i in range(pass_len):
    password += random.choice(charValue)

print("Your password is :",password)

import os 
cwd = os.getcwd() 
print("Current working directory:", cwd)