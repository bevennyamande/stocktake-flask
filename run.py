#!/usr/bin/env python

from stock_taking_app import *
DEBUG = True  # Turns on debugging features in Flask

print("\n*****************************************************")
print("Stocktaking appliction for Museyamwa Store")
print("*****************************************************\n")

app.run(debug=DEBUG, host='0.0.0.0', port=80)
