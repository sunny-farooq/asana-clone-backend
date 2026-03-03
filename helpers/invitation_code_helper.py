import random
import string

def invitation_code_generator()-> str:
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choice(characters) for i in range(6))
    return random_string

print(invitation_code_generator())


