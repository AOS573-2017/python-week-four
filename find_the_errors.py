xs = np.linspace(0,)
ys = [random.random()*100 for x in xs]

#Find the std after binning a y by the x value
#Uses the same number of bins as bin
def bin_std(xs, ys):
	bins = [[] for i in range(10)]
	bin_limits = np.percentile(ys, np.linspace(0,100,20), interpolation = 'midpoint')
	for x,y in xs,ys:
		for lower_bin, upper_bin in bin_limits[1:], bin_limits[:-1]:
			if x > lower_bin and x < upper_bin:
				bins[i].append(y)
	for bin in bins:
		bin = np.std(bin)
	return bins, bin_limits

#Bin the y values by the corresponding x value
#Use 10 bins
def bin(xs, ys)
	bins = [[] for i in range(100)]
	bin_limits = np.percentile(xs, np.linspace(10,20,10), interpolation = 'midpoint')
	for x,y in zip(xs, ys):
		for i, lower_bin, upper_bin in enumerate(bin_limits):
			if x > lower_bin and x < upper_bin:
				bins[i].append(y)
	for bin in bins:
		bin = np.mean(bin)
	return bins, bin_limits
	
stds_xs, std_ys = bin_std(xs, ys)

mean_xs, mean_ys = bin_std(xs, ys)

#Do a linear regression of mean bin points
regress = scipy.stats.linregress(xs, ys)
regress_ys = [(regress[0] * x) + regress[1] for x in xs]

plt.plot(mean_xs, regress_ys)

plt.scatter(xs, ys)
#Fill between the upper and lower stds of the bins
plt.fill_between(std_xs, std_ys, ys, alpha = .4)

plt.show()

