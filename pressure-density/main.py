

radius_list = [] #r
density_list = [] #rho
pressure_list = [] #p

n = 6 #just for now for testing purposes, but will ask user for range
m = 2 #just for testing purposes, but will ask user for steps

#below building radius list
for number in xrange(1, (n+1), m):
  radius_list.append(number)

print "Your generated radius list is", "\n", radius_list
