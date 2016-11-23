# stocktake-flask
Stocktaking using Flask &amp; Peewee

This is app whose aim is to aid in stocktaking process that happens in normal business processes. 
Some of its objectives are:
	- Shorten the time it takes to conduct a stocktake or inventory count
	- Collate the data from various enumerators in the shorten time possible
	- Increase the accuracy of result of an inventory count event.
	- Make it easier to detect discrepencies between inventory records and physical quantities
It a presentation for Zimbabwe's 1st Pycon zw.pycon.org

Prerequisites

The application can be run on either Windows, Apple Mac or Linux. The computer should have Python 3 installed. If you are using 
python 2, you will have to go into the code and make the necessary changes. For installing the required addon libraries you may need
to install a packge manager such as pip

Installation

The application uses Flask, Flask-WTF and Peewee. These need to be installed in the python installation or virtual environment.
The easiest way to install them is to run the following command in  app directory:

	pip install -r requirements.txt
	
	
Deployment
This application has been created with the aim of setting up a temporary interface to record figures for stock take processes
Add additional notes about how to deploy this on a live system


Built With

    Flask - http://flask.pocoo.org/ micro web development framework for Python. 
    Flask-WTF - https://flask-wtf.readthedocs.io Simple integration of Flask and WTForms, including CSRF, file upload and Recaptcha integration.
    Peewee - http://docs.peewee-orm.com Peewee is a simple and small ORM. It has few (but expressive) concepts, making it easy to learn and intuitive to use.

Contributing
	
