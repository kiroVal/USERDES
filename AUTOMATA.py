import random
import string

def generate_string():
    while True:
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(9))
        if s.count('a') % 2 == 1:
            return s + '0'

language = [generate_string() for _ in range(5)]
for s in language:
    print(s)