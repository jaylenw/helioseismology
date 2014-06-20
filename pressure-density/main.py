from builders import density #importing density fxn from builders file
from builders import pressure #'                                      '
from plotting import plotr_rho #importing plotr_rho fxn from plotting file
from plotting import plotr_p   # '                                  '
from plotting import plotp_rho # '                                  '

radius_list = [] #r radius in meters
rho_list = [] #rho
pressure_list = [] #p

n = raw_input("Please enter an integer for the range for the radius in meters: ")
n = int(n) #converting to int

m = raw_input("Please enter an integer for iterating steps to calculate along the radius (meters): ")
m = int(m)

#below building radius list
for number in xrange(1, (n+1), m):
  radius_list.append(number) #adding numbers to radius list

print "Your generated radius list is", "\n", radius_list

j = len(radius_list) #obtaining length of radius list for list building below

for number in xrange(0, j):

  rho_list.append(density(radius_list[number])) #building density list full of rhos
  pressure_list.append(pressure(radius_list[number])) #building pressure list full of p's


print "Our density list is...", "\n", rho_list
print "Our pressure list is...", "\n", pressure_list

"""Plotting relationships using functions from plotting.py"""

plotr_rho(radius_list, rho_list) #plotting radius vs. density
plotr_p(radius_list, pressure_list)  #plotting radius vs. pressure
plotp_rho(pressure_list, rho_list)   #plotting pressure vs. rho
