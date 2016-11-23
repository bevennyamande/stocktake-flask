'''
This script is used to export the total number of per individual stock  item
into a CSV file which you can now open in excel.
'''
import time
from models import *

ProductTotal = {}
current_item = {}

# create totals table & fill with product data
print('\n\nCreate table to store totals......')
#database.drop_table(ProductTotal, fail_silently=True)
#database.create_tables([ProductTotal, ])
print('\n\nAdd individual products to table......')
for item in Product.select():
    ProductTotal[item.code] = {}
    ProductTotal[item.code]['code'] = item.code
    ProductTotal[item.code]['name'] = item.name
    ProductTotal[item.code]['total'] = 0


# Compute totals for each individual item
print("\n\nAdding up the totals for each product")
for pcount in ProductCount.select():
    ProductTotal[pcount.product.code]['total'] = 0 + pcount.count


# Export to CSV file
t = time.localtime()
filename = 'Stock Levels ' + time.asctime(t) + '.csv'
filename = filename.replace(' ', '_')
filename = filename.replace(':', '-')
export_file = open(filename, "w")
print('\n\nNow exporting results......')
for key in ProductTotal.keys():
    if ProductTotal[key]['total'] > 0:
        status_line = ProductTotal[key]['code'] + ', '
        status_line += ProductTotal[key]['name'] + ', '
        status_line += str(ProductTotal[key]['total']) + '\n'
        print(status_line)
        export_file.write(status_line)
export_file.close()
print('Exporting of results to {} done'.format(filename))