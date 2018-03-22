import matplotlib.pyplot as plt


class Plotter:

    def plot_histogram(self, y_axis, x_label='', y_label='', title=''):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        self.set_plot_style(x_label, y_label, title)

        result = plt.hist(y_axis, bins='fd', color='blue',
                          edgecolor='black', alpha=.75)
        plt.show()
        return result

    def set_plot_style(self, x_label, y_label, title):
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
