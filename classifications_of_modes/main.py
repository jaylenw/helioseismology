from gamma1 import omegaP #importing omegaP fxn from gamma1 file
from gamma1 import omegaG # '                                  '

"""
    If using my mental model from quantum correctly
    and applying it to finding p and g modes of radial oscillations, 'n' is the
    energy mode (energy level). 'l' is the angular degree.  The rotation
    splitting modes and angular degrees all depend on 'n'.

"""

#for now testing for n=5, will ask for user input later
n=5
i=0 #used for iterations and indexing

print "Energy mode is",n,"."

#initializing lists for angular and splitting modes
m_list = []      #splitting modes
l_list = []      #angular modes
omegaP_list = [] #omega for p modes


#below we are building the angular energy mode
for number in xrange(0, (n+1)):

    l_list.append(number) #adding numbers to list

print "Angular degrees are...", "\n", l_list


#below we are building the rotation splitting modes, 'm' , known as m
for number in xrange((-1*n), (n+1)):

    m_list.append(number)

print "Rotation splitting modes are...", "\n", m_list




for number in xrange(0, (n+1)):

  #going to capture answer for omega

  l = l_list[i] #specific angular mode in the angular mode list
  omegaP_list.append(omegaP(n, l)) #building the omegaP_list

  i+=1 #i is incrementing by one

print "Omegas for a given 'n' that are p modes are...", "\n", omegaP_list
