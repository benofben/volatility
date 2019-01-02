import csv

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

def sequence_dates():
    print('Sequencing dates...')

def run():
    #consolidate()
    normalize()
    withhold()
    sequence_dates()

run()
