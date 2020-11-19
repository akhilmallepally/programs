import random

lowercase = 'abcdefghijklmnopqrstuvwxyz'

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numbers = '0123456789'

specialchar = '!@$&[]{},./:;*-_'

all = lowercase + uppercase + numbers + specialchar

length = 16
password = "".join(random.sample(all, length))

print(password)