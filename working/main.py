from gamma1 import omegaP #importing omegaP fxn from gamma1 file
from gamma1 import omegaGsquared # '                                  '
from gamma1 import omegaG # '                                  '
from plotting import plotomegaP #importing plotomegaP fxn from plotting file
from plotting import plotomegaGsqrd # '                                  '
from plotting import plotomegaG # '                                  '

"""
    If using my mental model from quantum correctly
    and applying it to finding p and g modes of radial oscillations, 'n' is the
    energy mode (energy level). 'l' is the angular degree.  The rotation
    splitting modes and angular degrees all depend on 'n'.

"""

#Below asking user for input on angular degree

n = raw_input( "Please enter a number for the radial order: ")
n = int(n)

"""In python 2.7, it is recommended to take user input using raw_input
and then I'm converting the string into an int"""

i=0 #used for iterations and indexing

print "Energy mode is",n,"."

#initializing lists for angular and splitting modes
m_list = []      #splitting modes
l_list = []      #angular modes
omegaP_list = [] #omega for p modes
omegaGsqrd_list = [] #omega squared for g modes
omegaG_list = [] #omega for g modes


#below we are building the angular energy mode
for number in xrange(0, (n+1)):

    l_list.append(number) #adding numbers to list

print "Angular degrees are...", "\n", l_list


#below we are building the rotation splitting modes, 'm' , known as m
for number in xrange((-1*n), (n+1)):

    m_list.append(number)  #adding numbers to list

print "Rotation splitting modes are...", "\n", m_list




for number in xrange(0, (n+1)):

  #going to capture answer for omega

  l = l_list[i] #specific angular mode in the angular mode list
  omegaP_list.append(omegaP(n, l)) #building the omegaP_list
  omegaGsqrd_list.append(omegaGsquared(n, l)) #building the omegaGsquared_list
  omegaG_list.append(omegaG(omegaGsquared(n, l))) #building the omegaG list

  i+=1 #i is incrementing by one

print "Omegas for a given 'n' that are p modes are...", "\n", omegaP_list

print "Omega squared for a given 'n' that are g modes are...","\n", omegaGsqrd_list

print "Omegas for a given 'n' that are g modes are...", "\n", omegaG_list

"""below using the plot functions in plotting.py to plot the angular degree
list and the omega lists"""

plotomegaP(l_list, omegaP_list)

plotomegaGsqrd(l_list, omegaGsqrd_list)

plotomegaG(l_list, omegaG_list)
