import string
import random

def token_generator(size=50, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

print(token_generator())