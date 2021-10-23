import os.path
import string
from random import randint, choice

ps = string.ascii_letters + string.punctuation + string.digits

print("".join(choice(ps) for x in range(15)))