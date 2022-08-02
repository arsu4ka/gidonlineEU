from random_username.generate import generate_username
import secrets
import string
import random

def username_gen():
    '''
    Func to generate random username
    '''

    return generate_username()[0]


def password_gen():
    '''
    Func to generate random password
    '''

    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(random.randint(10, 15)))
    return password
