""" If using my mental model from quantum correctly
    and applying it to finding p and g modes of radial oscillations, 'n' is the
    energy mode (energy level). 'l' is the angular degree.  The rotation
    splitting modes and angular degrees all depend on 'n'.

"""


n=4
m_list = []
l_list = []

#below we are building the rotation splitting modes, 'm' , known as m
for number in xrange((-1*n), (n+1)):

    m_list.append(number)
    print number


print m_list

#below we are building the angular energy mode
for number in xrange(0, (n+1)):

    l_list.append(number)

print l_list
