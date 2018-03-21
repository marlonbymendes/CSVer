
# %load app.py
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

class CSVer:
    
    DATE_INPUT_FORMAT = '%Y-%m-%d %H:%M:%S'
    DATE_OUTPUT_FORMAT = '%m/%Y'
    DATE_GRAPH_FORMAT = DATE_OUTPUT_FORMAT
    
    ITEMS_COLUMN = 'Item'
    DATES_COLUMN = 'Data'
    #VALUES_COLUMN = 'ValorUnitarioSolicitado'
    VALUES_COLUMN = 'ValorUnitarioAprovado'
    
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
        return self.csv[self.csv[column] == value]
    
    def get_date_axis_from_column(self, data_frame = None, column = 'Data'):
        if data_frame is None:
            data_frame = self.csv

        dates = data_frame[column].values
        dates_date_time = [datetime.strptime(d, CSVer.DATE_INPUT_FORMAT) for d in dates]
        dates_axis = matplotlib.dates.date2num(dates_date_time)
        return dates_axis

    def plot_histogram(self, y_axis, x_label = '', y_label = '', title = ''):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        plt.setp(ax.get_xticklabels(), rotation=15)
        plt.hist(y_axis, 50)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()
    
    def plot_y_axis_along_time(self, x_axis, y_axis, x_label = '', y_label = '', title = ''):
        hfmt = matplotlib.dates.DateFormatter(CSVer.DATE_GRAPH_FORMAT)
        fig = plt.figure()
        ax = fig.add_subplot(1,2,1)
        ax.xaxis.set_major_formatter(hfmt)
        plt.setp(ax.get_xticklabels(), rotation=15)
        plt.scatter(x_axis, y_axis, s = 50, c = 'blue', alpha = 0.25)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

        ax = fig.add_subplot(1,2,2)
        ax.xaxis.set_major_formatter(hfmt)
        plt.setp(ax.get_xticklabels(), rotation=15)
        plt.semilogy(x_axis, y_axis, '.')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()

    
    def plot_item_value_along_time(self, item):
        rows = self.filter_column_by_value(CSVer.ITEMS_COLUMN, item)
        x = csver.get_date_axis_from_column(data_frame = rows, column = CSVer.DATES_COLUMN)
        y = rows[CSVer.VALUES_COLUMN].values
        csver.plot_histogram(y, 'Data (dia/mes/ano)', 'Valor unitário solicitado (R$)', item)
        print('Ploting item \"{}\"...'.format(item))
    
    def plot_random_item_value_along_time(self):
        distinct_items = self.get_distinct_rows(CSVer.ITEMS_COLUMN)
        item = np.random.choice(distinct_items)
        self.plot_item_value_along_time(item)
       
if __name__ == '__main__':
    csv_file_name = 'APROVADO.csv'
    csver = CSVer(file_name = csv_file_name)
    dt = csver.csv
    distinct = dt['Item'].unique()
    while True:
        csver.plot_random_item_value_along_time()
