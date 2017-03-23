import matplotlib.pyplot as plotter

data_coord_x = [1, 2, 3, 4]
data_coord_y = [2, 7, 14, 3]
labels = ['alef', 'bet', 'ce', 'doo']
plotter.plot(data_coord_x, data_coord_y, 'o')
plotter.xticks(data_coord_x, labels)
plotter.show()
