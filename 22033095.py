import csv
import numpy as np
import matplotlib.pyplot as plt

# read data from CSV file
data = []
with open('data5.csv', 'r') as file:
    reader = csv.reader(file)
    ##next(reader)  # skip header row
    for row in reader:
        data.append(float(row[0]))

# create histogram of newborn weights
weights, bins  = np.histogram(data, bins = 20, range = (0, 10))
bin_centers = (bins[:-1] + bins[1:]) / 2

# calculate mean weight and X
mean_weight = np.mean(data)
weights_mean = np.sum(weights[np.logical_and(bin_centers >= 0.8 * mean_weight, bin_centers <= 1.2 * mean_weight)])
frac_mean = weights_mean / len(data)

# plot histogram and print mean weight and X
plt.figure(figsize = (9, 5), layout = "constrained")
plt.hist(data, bins = 33, range = (1, 5), alpha = 0.5, color = 'blue',edgecolor='black')
plt.axvline(mean_weight, color='r', linestyle = 'dashed', linewidth = 1)
plt.axvspan(0.8 * mean_weight, 1.2 * mean_weight, alpha = 0.5, color = 'green')
plt.xlabel('Newborn weight (kg)')
plt.ylabel('Frequency')
plt.title('Distribution of Newborn Weights')
plt.legend(['Mean weight', '0.8W-1.2W'])
plt.text(5.5, 20, 'Mean weight: {:.2f} kg\nFraction 0.8W-1.2W: {:.2f}'.format(mean_weight, frac_mean))
plt.show()
plt.close()
