import numpy as np
import pandas as pd

class CSVer:

    def __init__(self, file_name, nrows = None):
        self.csv = pd.read_csv(file_name, nrows = nrows)

    def get_first_n_rows(self, n):
        return  self.csv.head(n)

    def get_column(self, column_name):
        return self.csv[column_name]

    def get_distinct_rows(self, column_name):
        distinct_rows = self.get_column(column_name).unique()
        return distinct_rows

    def filter_column_by_value(self, column, value):
        return self.csv.loc[self.csv[column] == value]

    def filter_column(self, **kwargs):
        return self.csv.loc[self.csv[column] == value]

name = 'SOLICITADO.csv'
n = 1000
csver = CSVer(file_name = name, nrows = n)
