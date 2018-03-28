from csver import CSVer
from plotter import Plotter
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class SalicPlotter:

    ITEM_COLUMN = 'Item'
    DATE_COLUMN = 'Data'

    REQUESTED_COLUMN = 'ValorUnitarioSolicitado'
    APPROVED_COLUMN = 'ValorUnitarioAprovado'

    def __init__(self, csv_names):
        self.csver = CSVer(csv_names)

    def plot_random_item_on_time(self, y_column, csv_pos = 0):
        csver = self.csver
        item = csver.get_random_item(SalicPlotter.ITEM_COLUMN, csv_pos)
        x, y = csver.get_x_y(SalicPlotter.DATE_COLUMN, y_column, (SalicPlotter.ITEM_COLUMN, item),
                             csv_pos)
        x_dates = csver.get_date_axis_from_array(x)

        plotter = Plotter()
        plotter.plot_scatter_along_time(x_dates, y, 'blue', SalicPlotter.DATE_COLUMN,
                                        y_column, item)
        plotter.show()

    def setup_requested_vs_approved(self, item):
        csver = self.csver
        x1, y1 = csver.get_x_y(SalicPlotter.DATE_COLUMN, SalicPlotter.REQUESTED_COLUMN,
                               (SalicPlotter.ITEM_COLUMN, item), 0)
        x1 = csver.get_date_axis_from_array(x1)

        x2, y2 = csver.get_x_y(SalicPlotter.DATE_COLUMN, SalicPlotter.APPROVED_COLUMN,
                               (SalicPlotter.ITEM_COLUMN, item), 1)
        x2 = csver.get_date_axis_from_array(x2)

        return [(x1, y1), (x2, y2)]

    def plot_requested_vs_approved(self, item):

        requested_axis, approved_axis = self.setup_requested_vs_approved(item)
        x1, y1 = requested_axis
        x2, y2 = approved_axis

        fig = plt.figure()
        plotter = Plotter()

        red_patch = mpatches.Patch(color='red', label='Solicitado')
        green_patch = mpatches.Patch(color='green', label='Aprovado')
        plt.legend(handles=[red_patch, green_patch])

        plotter.plot_scatter_along_time(x1, y1, 'red', marker = '*', figure = fig)
        plotter.plot_scatter_along_time(x2, y2, 'green', 'Data (dia/mes/ano)',
                                        'Custo Unitário (R$)', item, figure=fig)
        plotter.show()

    def plot_requested_vs_approved_log(self, item):
        requested_axis, approved_axis = self.setup_requested_vs_approved(item)
        x1, y1 = requested_axis
        x2, y2 = approved_axis

        fig = plt.figure()
        plotter = Plotter()

        red_patch = mpatches.Patch(color='red', label='Solicitado')
        green_patch = mpatches.Patch(color='green', label='Aprovado')
        plt.legend(handles=[red_patch, green_patch])

        plotter.plot_log_along_time(x1, y1, '.r', figure=fig)
        plotter.plot_log_along_time(x2, y2, '.g', 'Data (dia/mes/ano)', 'Custo Unitário (R$)',
                                    item, figure=fig)
        plotter.show()

small_data = ['solicitado_small.csv', 'aprovado_small.csv']
big_data = ['SOLICITADO.csv', 'APROVADO.csv']

sp = SalicPlotter(big_data)

while True:
    item = sp.csver.get_random_item(SalicPlotter.ITEM_COLUMN)
    sp.plot_requested_vs_approved(item)

