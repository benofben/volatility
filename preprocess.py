import csv
from datetime import datetime

def consolidate():
    print('Consolidating...')
    with open('data/consolidated.csv', 'w') as output:
        for index in range(1,3):
            filename = 'raw_data/stock_prices_uscomp_since_2008-01-01_file-' + str(index) + '.csv'
            with open(filename) as input:
                for line in input:
                    # Only print one header row
                    if index != 1 and line.startswith('SECURITY_ID,TICKER'):
                        pass
                    else:
                        output.write(line)

def normalize():
    print('Normalizing...')
    with open('data/normalized.csv', 'w') as output:
        writer = csv.writer(output)
        output_row=['TICKER', 'DATE', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'LABEL']
        writer.writerow(output_row)

        with open('data/consolidated.csv') as input:
            reader = csv.DictReader(input)
            for row in reader:
                try:
                    o=float(row['OPEN'])
                    h=float(row['HIGH'])
                    l=float(row['LOW'])
                    c=float(row['CLOSE'])
                    v=float(row['VOLUME'])

                    n_high=round(h/o*100,2)
                    n_low=round(l/o*100,2)
                    n_close=round(c/o*100,2)
                    n_volume=round(v*o/1000000,2)

                    if h/o>1.02:
                        label=True
                    else:
                        label=False

                    # drop data points with less than $10m in volume
                    if n_volume>10:
                        output_row=[row['TICKER'], row['DATE'], n_high, n_low, n_close, n_volume, label]
                        writer.writerow(output_row)

                except ValueError:
                    pass

def withhold():
    print('Withholding...')

    file={}
    writer={}
    filenames=['train', 'test', 'withhold']
    output_row=['TICKER', 'DATE', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'LABEL']

    for filename in filenames:
        file[filename]=open('data/'+ filename + '.csv', 'w')
        writer[filename] = csv.writer(file[filename])
        writer[filename].writerow(output_row)

    with open('data/normalized.csv') as input:
        reader = csv.DictReader(input)
        for row in reader:
            d=row['DATE']
            d=datetime.strptime(d, '%Y-%M-%d')
            year=d.year

            row=[row['TICKER'], row['DATE'], row['HIGH'], row['LOW'], row['CLOSE'], row['VOLUME'], row['LABEL']]
            if year<2012:
                writer['train'].writerow(row)
            elif year<2015:
                writer['test'].writerow(row)
            else:
                writer['withhold'].writerow(row)

    for filename in filenames:
        file[filename].close()

def run():
    consolidate()
    normalize()
    withhold()

run()
