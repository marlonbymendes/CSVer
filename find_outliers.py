from csver import CSVer
from plotter import Plotter
from sklearn.neighbors import LocalOutlierFactor

class FindOutliers:

    def __init__(self, training_data):
        self.training_data = training_data

    def train(self):
        self.lof = LocalOutlierFactor()
        self.lof_labels = self.lof.fit_predict()
        return self.lof_labels

data = ['aprovado_small.txt']
csver = CSVer(data)
item = csver.get_random_item('Item')
dt_item = csver.filter_column_by_value('Item', item)