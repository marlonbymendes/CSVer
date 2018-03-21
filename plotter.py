class Plotter:

  def plot_histogram(self, y_axis, x_label = '', y_label = '', title = ''):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        plt.setp(ax.get_xticklabels(), rotation=15)
        plt.hist(y_axis, bins = 'auto')
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()
