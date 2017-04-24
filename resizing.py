#!usr/bin/env python
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from scipy import interpolate
import numpy as np
import numpy.ma as ma
from netCDF4 import Dataset
import sys
import json
#Our example file is in python-week-four
filename = 'temp.nc'
#Open the dataset
#It is CERES EBAF clear sky fluxes btws
fluxes_data = Dataset(filename, mode = 'r')
#This is the data before any regridding
before = fluxes_data['solar_mon'][:][6]

with open('example.txt', 'r') as f:
	temp = json.load(f)
	print np.array(temp['data']).shape
sys.exit()
'''

temp_data = {'data': [[float(l) for l in b] for b in before], 'lat': [float(l) for l in fluxes_data['lat'][:]], 'lon': [float(l) for l in fluxes_data['lon'][:]]}
with open('example.txt', 'w') as f:
	json.dump(temp_data, f)
sys.exit()'''
#Create a function
#This takes in the lon, lat, and data as it is and creates a function that can interpolate this data to any new grid size now
function = interpolate.interp2d(fluxes_data['lon'][:], fluxes_data['lat'][:], before, kind = 'linear')
#Create a set of new lats and lons to increase our resolution
new_lon = np.linspace(-179.5, 179.5, 720)
new_lat = np.linspace(-79.5, 79.5, 360)
#This is the new 2d data at a higher resolution made using the defined function and our lat/lon lists
new = function(new_lon, new_lat)

#This code is for plotting
#To plot using Basemap you must download it from source
#Information on downloading and installing modules from source can be found in 
#Week 2 lecture notes
#Create a basemap telling matplotlib what your lower left corner lat will be, the upper right corner lon, the lower left corner lon, and the upper right corner lon of the map 
m = Basemap(projection = 'gall',  llcrnrlat=-90,urcrnrlat=90,  llcrnrlon=-180, urcrnrlon=180, resolution = 'c')
#Draw on some coastlines
m.drawcoastlines()

#Define a grid of the new resolution data
plot_lon, plot_lat = np.meshgrid(new_lon, new_lat)
#Then pass this to the map object to get xs and ys for plotting
xi, yi = m(plot_lon, plot_lat)
#Now pass in xs, ys, and the new data on the map
m.pcolor(xi, yi, new)
#Add a colorbar
plt.colorbar()
#Show the plot
plt.show()

