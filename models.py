'''
This file contains definitions for the models. These are by peewee to create the
necessaary database tables into which our products will be stored. To create the
database and associated table please run this file directly with python
'''

import datetime
from peewee import *


# Name of Database file. Please change it to suitable representation
DATABASE = 'db.sqlite3'

# create a peewee database instance -- our models will use this database to
# persist information
database = SqliteDatabase(DATABASE)


# model definitions -- the standard "pattern" is to define a base model class
# that specifies which database to use.  then, any subclasses will automatically
# use the correct storage. for more information, see:
# http://charlesleifer.com/docs/peewee/peewee/models.html
class BaseModel(Model):
    class Meta:
        database = database


# This is where we store user credentials
class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    created = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        order_by = ('username',)


# This model holds the definitions of the product in the store
class Product(BaseModel):
    code = CharField(unique=True)
    name = CharField()
    price = DecimalField()
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        order_by = ('name',)

    def details(self):
        # return a description of product
        return self.code + ' : ' + self.name + ' - $' + str(self.price)


# This model is used to hold all product counts. One product may have many count
# occurances. They are added up to get a total for the report.
class ProductCount(BaseModel):
    count = IntegerField()
    product = ForeignKeyField(Product, related_name='product')
    counted_by = ForeignKeyField(User, related_name='user')
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        order_by = ('created',)



# simple utility function to create database and fill it with blanktables
def create_tables():
    database.connect()
    database.create_tables([User, Product, ProductCount])


if __name__ == '__main__':
    create_tables()
    print("Database has been created, ready for filling up")