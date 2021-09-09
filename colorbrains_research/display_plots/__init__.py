import os


datapath = os.path.join(os.path.dirname(__file__), 'plots')
if not os.path.exists(datapath):
    os.makedirs(datapath)


def get_plot_path(filename):
    return os.path.join(datapath, filename)
