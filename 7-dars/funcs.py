import string
import random

def create_password():
    return "".join(random.sample(string.ascii_letters+string.digits, 8))