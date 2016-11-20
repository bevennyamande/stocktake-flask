'''
This script is used to add stock take counters.
'''
from models import *


fo = open("users.csv", "r+")

lines = fo.readlines()
fo.close()
for line in lines:
    line = line.strip('\n')
    line_fields = line.split(',')
    username = line_fields[0]
    password = line_fields[1]
    admin = line_fields[2]
    username = username.strip()
    password = password.strip()
    admin = admin.strip()
    admin = admin.lower()

    # search if user is already in database else create user
    try:
        user = User.get(User.username == username)
    except User.DoesNotExist:
        if admin == 'y':
            is_admin = True
        else:
            is_admin = False
        user = User.create(username=username, password=password,
            is_admin=is_admin)

        print("Created user : {} -  admin : {} ".format(user.username, admin))