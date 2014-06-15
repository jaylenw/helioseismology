from builders import density #importing density fxn from builders file
from builders import pressure #'                                      '
from plotting import plotr_rho #importing plotr_rho fxn from plotting file
from plotting import plotr_p   # '                                  '
from plotting import plotp_rho # '                                  '

radius_list = [] #r radius in meters
rho_list = [] #rho
pressure_list = [] #p

n = 6 #just for now for testing purposes, but will ask user for range
m = 2 #just for testing purposes, but will ask user for steps

#below building radius list
for number in xrange(1, (n+1), m):
  radius_list.append(number) #adding numbers to radius list

print "Your generated radius list is", "\n", radius_list

n = len(radius_list) #obtaining length of radius list for list building below

for number in xrange(1, (n+1)):

  rho_list.append(density(number)) #building density list full of rhos
  pressure_list.append(pressure(number)) #building pressure list full of p's


print "Our density list is...", "\n", rho_list
print "Our pressure list is...", "\n", pressure_list

"""Plotting relationships using functions from plotting.py"""

plotr_rho(radius_list, rho_list) #plotting radius vs. density
plotr_p(radius_list, pressure_list)  #plotting radius vs. pressure
plotp_rho(pressure_list, rho_list)   #plotting pressure vs. rho
