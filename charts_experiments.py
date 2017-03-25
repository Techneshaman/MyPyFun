import matplotlib.pyplot as plotter
import random

# Let's make a cloud out of any selected distributions and parameters and plot them in a single figure

x_coord_list = []
y_coord_list = []

AMONUT_OF_POINTS = 300

functions_dict = {'normal': random.gauss,
                  'uniform': random.uniform,
                  'triangular': random.triangular
                  }

functions_param_dict = {'normal': (0, 1),
                        'uniform': (-3, 3),
                        'triangular': (-3, 3, 0.6)}

charts_matrix = []

for x in functions_dict:
    for y in functions_dict:
        chart_x = x
        chart_y = y
        charts_matrix.append((chart_x, chart_y))

print(charts_matrix)

amount_of_charts = len(functions_dict)**2
axes_sizes = len(functions_dict)

subplots_positions = []

for chart_number in range(1, amount_of_charts+1):
    subplot_pos = axes_sizes*110 + chart_number
    subplots_positions.append(subplot_pos)

plot_position = 0

for item in charts_matrix:
    x_coord_list = []
    y_coord_list = []

    for i in range(AMONUT_OF_POINTS):
        function_x = functions_dict[item[0]]
        function_y = functions_dict[item[1]]

        function_x_params = functions_param_dict[item[0]]
        function_y_params = functions_param_dict[item[1]]

        coord_x = function_x(*function_x_params)
        coord_y = function_y(*function_y_params)

        x_coord_list.append(coord_x)
        y_coord_list.append(coord_y)

    plotter.subplot(subplots_positions[plot_position])
    plot_position += 1
    plotter.plot(x_coord_list, y_coord_list, 'o')
    plotter.title(item)

plotter.show()
