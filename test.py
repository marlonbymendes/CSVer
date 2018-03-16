import numpy as np
import pandas as pd

#FILE_SOLICITADO = 'SOLICITADO.csv'
#solicitado_df = pd.read_csv(FILE_SOLICITADO)

FILE_APROVADO = 'APROVADO.csv'
COLUMN_ITEM = 'Item'
aprovado_df = pd.read_csv(FILE_APROVADO)

df = aprovado_df
items = set()
for index, obj in df.iterrows():
    items.add(obj[COLUMN_ITEM])

print('Items = {}'.format(len(items)))
