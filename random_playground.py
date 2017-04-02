import random
import matplotlib.pyplot as plotter


# proper use of shuffle. Note: print(random.shuffle(data)) will NOT work, shuffle OVERWRITES it

data = [1,2,3,4,5]

print("Input list:", data)
random.shuffle(data)
print("Shuffled list:", data)

data2 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print('Input list of lists:', data2)
random.shuffle(data2)
print('Shuffled list of lists:', data2)

# looks like documentation is wrong? random.choices doesn't exist for python 3.5. Use random.sample instead or sth.

print("Random element of input list:", random.choice(data))
print("Random element of input list of lists:", random.choice(data2))
print('K random numbers from selected range:', random.sample(range(100), k=2))

# some examples for random drawings from different distributions. NICE

sample_size = 1000

i = 0
samples = {'normal': [],
           'uniform': [],
           'triangular': [],
           'lognormal': []}
while i < sample_size:
    i += 1
    normal_draw = random.gauss(0,1)
    uniform_draw = random.uniform(0,1)
    triangular_draw = random.triangular(0,1,0.8)
    lognormal_draw = random.lognormvariate(0,1)
    samples['normal'].append(normal_draw)
    samples['uniform'].append(uniform_draw)
    samples['triangular'].append(triangular_draw)
    samples['lognormal'].append(lognormal_draw)

positions = [221,222,223,224]
i = 0
for item in samples:
    plotter.subplot(positions[i])
    plotter.hist(samples[item], bins=19)
    plotter.title(item)
    i += 1

plotter.show()

# actually that's how positions work if I don't want them to be too fancy

grid_height = 2
grid_width = 2
amount_of_charts = 4

positions = []
for i in range (1, amount_of_charts+1):
    chart_position = grid_height * 100 + grid_width * 10 + i
    positions.append(chart_position)

i = 0
plotter.figure()
for item in samples:
    plotter.subplot(positions[i])
    plotter.hist(samples[item], bins=19)
    plotter.title(item)
    i += 1

plotter.show()
