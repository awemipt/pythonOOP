import random

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

def psw(psw_chars, min_length, max_length):
    def wrapper():
        return "".join([random.choice(psw_chars) for _ in range(random.randint(min_length,max_length))])
    return wrapper

s = psw(psw_chars, min_length, max_length)
print(s())