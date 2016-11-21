'''
This script is used to export the total number of per individual stock  item
into a CSV file which you can now open in excel.
'''
import time
from models import *

filename = str(time.time())

product_count = {}
current_item = {}

# Compute totals for each individual item
print("\n\nAdding up the totals for each product")
for item in ProductCount.select():
    try:
        current_item = product_count[item.product.code]
    except KeyError:
        current_item['name'] = item.product.name
        current_item['count'] = item.count
        product_count[item.product.code] = current_item
    else:
        current_item['count'] += item.count
        product_count[item.product.code] = current_item
    status_line = item.product.code + ' : ' + item.product.name + ' - '
    status_line += str(current_item['count'])
    print(status_line)

# Export to CSV file
t = time.localtime()
filename = time.asctime(t)
print(filename)
export_file = open("tt.csv", "w")
print('\n\nNow exporting results to')
for key in product_count.keys():
    item = product_count[key]
    status_line = key + ', ' + item['name'] + ', ' + str(item['count'])
    print(status_line)
    export_file.write(status_line)
    export_file.write('\n')

export_file.close()
print('Exporting of results to {} done'.format(filename))