import random

def password_generator():
    convalid = "s"
    while convalid == "s" or convalid == "S":
        counter()
        convalid = input('''For reuse the program press "s" or an another key: ''')

    print("Thanks you for use the program!")

def counter():
    print('''PASSWORD GENERATOR''')

    char = '''abcdefghilmnopqrstuvzxywkjABCDEFGHILMNOPQRSTUVZJKWLY123456789!?/][}{|@#$%^&*()-_=+'''

    lengt = int(input('''Choose the lenght of the password: '''))

    password = ''

    for x in range(lengt):
        password += random.choice(char)

    print("The password created: ", password)


password_generator()