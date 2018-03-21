from csver import CSVer

approved = 'aprovado_small.csv'
csvs = [approved]

csver = CSVer(csvs)
item = csver.get_random_item('Item')
csver.filter_column_by_value('Item', item)

