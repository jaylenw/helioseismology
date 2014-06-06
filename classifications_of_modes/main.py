from gamma1 import omegaP #importing gamma_1 fxn from gamma1 file

"""
    If using my mental model from quantum correctly
    and applying it to finding p and g modes of radial oscillations, 'n' is the
    energy mode (energy level). 'l' is the angular degree.  The rotation
    splitting modes and angular degrees all depend on 'n'.

"""


n=5

print "Energy mode is",n,"."

#initializing lists for angular and splitting modes
m_list = []      #splitting modes
l_list = []      #angular modes


#below we are building the angular energy mode
for number in xrange(0, (n+1)):

    l_list.append(number)

print "Angular degrees are...", "\n", l_list


#below we are building the rotation splitting modes, 'm' , known as m
for number in xrange((-1*n), (n+1)):

    m_list.append(number)

print "Rotation splitting modes are...", "\n", m_list




for number in xrange(0, (n+1)):

  #going to capture answer for omega
