import random
import string

len = 6
OTP = ""
Character = string.ascii_letters + string.digits

for i in range(len):
    OTP = OTP + random.choice(Character)

print(f"OTP is: {OTP}")