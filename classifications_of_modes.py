""" If using my mental model from quantum correctly
    and applying it to finding these modes, 'n' is the energy mode (energy
    level). 'l' is the angular degree.  The rotation splitting modes and angular
    degrees all depend on 'n'.

"""


n=4
N = ((-1*n) -1)
m_list = []

#below we are building the rotation splitting, 'm' , known as m
for number in xrange(n, N, -1):

    m_list.append(number)
    print number


print m_list

print N
