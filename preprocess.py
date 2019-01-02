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
                open=float(row['OPEN'])
                high=float(row['HIGH'])
                low=float(row['LOW'])
                close=float(row['CLOSE'])
                volume=float(row['VOLUME'])

                n_high=round(high/open*100,2)
                n_low=round(low/open*100,2)
                n_close=round(close/open*100,2)
                n_volume=round(volume*open/1000000,2)

                if high/open>1.02:
                    label=True
                else:
                    label=False

                output_row=[row['TICKER'], row['DATE'], n_high, n_low, n_close, n_volume, label]
                writer.writerow(output_row)

                # Unclear how to normalize date.  Need to think about this...

def withhold():
    print('Withholding...')
    pass

def run():
    #consolidate()
    normalize()
    withhold()

run()
