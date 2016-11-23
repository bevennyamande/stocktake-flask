# Stocktake-Flask-Peewee
## Stocktaking using Flask &amp; Peewee

This is app whose aim is to aid in stocktaking process that happens in normal business processes. 
Some of its objectives are:
	- Shorten the time it takes to conduct a stocktake or inventory count
	- Collate the data from various enumerators in the shorten time possible
	- Increase the accuracy of result of an inventory count event.
	- Make it easier to detect discrepencies between inventory records and physical quantities
Its a presentation for Zimbabwe's 1st [Pycon](http://zw.pycon.org)

## Prerequisites

The application can be run on either Windows, Apple Mac or Linux. The computer should have Python 3 installed, it hasn't been tested on Python 2. 
If you are using python 2, you will have to go into the code and make the necessary changes. For installing the required addon libraries you will may need
to install a packge manager such as pip.

## Installation

The application uses Flask, Flask-WTF and Peewee. These need to be installed in the python installation or virtual environment.
The easiest way to install them is to run the following command in  app directory:

	pip install -r requirements.txt
	
	
## Deployment & Usage

This application has been created with the aim of setting up a temporary web interface to record figures during a stocktake. It will 
run using the internal WSGI. 

### Step 1:
Extract the files. Using command line navigate into the directory and excute the following command to setup the database. 
Default is to create an SQLite Database. But you can go into "models.sql" and change the database connection settings to point to an peewee 
supported database system. Execute the following command:

	python models.py


### Step 2:
Open users.csv and add users and their related passwords. The first column contains the enumerator's username. 
The second column contains that user's password. The second column defines whether the user will be an administrator.
Administrators for are able to see the products counted by each user, while users are only able to see their past enumerations. Save the file
as csv. Add the users to the database by executing the following command:

	python add_users.py

### Step 3:
Open products.csv and add the products that are found in stock. If you have an accounting system you can extract a file with the product
details. The first column contains the product code. The second column contains the product name. The third column contains the price of the
item. This is for reference purposes. After saving the  file import the products into the database by issuing the following command:

python add_products.py

### Step 4:
Connect the computer to a router or if you have the necessary software you can turn it into a wireless access point. 
Find the IP address of the computer on the network. You can refer to this [article](https://www.dowling.edu/mydowling/tech/ipaddress.html) or google it. 
This will be used by enumerators to connect to the application through their device browsers. Now execute the the web server by typing the following command:

python run.py

A webserver will be setup on your computer and can be accessed via "http://<ipaddress>:<port>/ the default port being 5000. Please
ensure the port u select is not being used by another application. Users can login using their usernames and password. Once logged
in they can select a product and enter its count. Various teams can access
the database at the same time.

### Step 5:
When all the products, turn of the server application by holding down 'Ctrl' Key and pressing 'C'(Ctrl+C). The records will now be 
in the database.

### Step 6:
Export the results of the stock count into a CSV file named 'export_stocklevels' and will have a time stamp. issue the following command

python export_stocklevels.py

You can now open the resulting file in Excel and do what you need to do with the data.

### Step 6:
Move onto next stocktake

## Built With

* [Flask](http://flask.pocoo.org/) a micro web development framework for Python. 
* [Flask-WTF](https://flask-wtf.readthedocs.io) Simple integration of Flask and WTForms, including CSRF, file upload and Recaptcha integration.
* [Peewee](http://docs.peewee-orm.com)Peewee is a simple and small ORM. It has few (but expressive) concepts, making it easy to learn and intuitive to use.

	
