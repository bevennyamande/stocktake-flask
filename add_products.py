'''
This script is used to add stock take counters.
'''

from decimal import Decimal
from models import *


fo = open("products.csv", "r+")

lines = fo.readlines()
fo.close()
count = 0
for line in lines:
    line = line.strip('\n')
    line_fields = line.split(',')
    code = line_fields[0]
    name = line_fields[1]
    price_string = line_fields[2]
    # strip spaces from start and end of string
    code = code.strip()
    name = name.strip()
    price_string = price_string.strip()
    # convert price from string to decimal
    price = Decimal(price_string)

    # search if product is already in database else create product
    try:
        product = Product.get(Product.code == code)
    except Product.DoesNotExist:
        product = Product.create(code=code, name=name, price=price)
        count = count + 1
        print("Created product number {} : {}".format(str(count),
                                                        product.details()))