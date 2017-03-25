import matplotlib.pyplot as plotter
import random

# Let's make a circlish cloud out of normal distribution

x_coord_list = []
y_coord_list = []

AMONUT_OF_POINTS = 1000

for i in range(AMONUT_OF_POINTS):
    coord_x = random.gauss(0,1)
    coord_y = random.gauss(0,1)

    x_coord_list.append(coord_x)
    y_coord_list.append(coord_y)

plotter.plot(x_coord_list, y_coord_list, 'o')
plotter.show()
