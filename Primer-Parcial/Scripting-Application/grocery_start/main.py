import csv

def write_list_of_dicts_to_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)
    
if __name__ == '__main__':
    dataSource = read_csv_to_dict('sample_grocery.csv')
    batchData = read_csv_to_dict('grocery_batch_1.csv')

    for dictB in batchData:
        for dictS in dataSource:
            if dictB['SKU'] == dictS['SKU']:
                print(f'same product found! ')
                print('SKU: ', dictS['SKU'], 'Actual quantity =', dictS['Quantity'])
                dictS['Quantity'] = int(dictS['Quantity']) + int(dictB['Quantity'])
                print('SKU: ', dictS['SKU'], 'updated quantity =', dictS['Quantity'])
                print('-'* 10)
                print('Updating Source list....')
    if dictB['SKU'] not in dataSource:
        print('The following SKU was not found: ', dictB['SKU'], ' --It will be added to source')
        dataSource.append(dictB)

    write_list_of_dicts_to_csv('grocery_db.csv',dataSource)

