from csver import CSVer
from plotter import Plotter
import matplotlib
import matplotlib.pyplot as plt

approved = 'aprovado_small.csv'
csvs = [approved]

csver = CSVer(csvs)
item = csver.get_random_item('Item')
dt = csver.filter_column_by_value('Item', item)
x, y = csver.get_x_y('Data', 'ValorUnitarioAprovado', ('Item', item))

plotter = Plotter()
arr = plotter.get_date_axis_from_array(x)
plotter.plot_scatter_log_along_time(arr, y, 'Data', 'ValorUnitario',
                                    item)
plotter.show()
