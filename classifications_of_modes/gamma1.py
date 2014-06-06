from math import sqrt #importing python built in math function

"""Gamma one

  I will be assuming the Sun is is made up of all hydrogen just to see how this
  works.  I will be using pressure and density that I looked up for the Sun.
  Although this may change.  Let's assume the Sun is made up of a monatomic
  ideal gas, therefore gamma = 5/3.

  (P*V)^gamma = constant, P is pressure, V is volume.

  gamma = ( C_sub(p) / C_sub(v) ) = ( f +2 / f ),

  where f is the number of degrees of freedom of the gas. For monoatomic case,
  the number of degrees of freedom are 3. so (2+3)/3 = 5/3
"""
gma1 = 5.0/3

#below we are finding omega for the p modes

def omegaP(n, l):
  omega_squared = (2*gma1*(n**2)) + (l*(l+1))/ (2*gma1*(n**2))
  omega = sqrt(omega_squared) #taking square root

  return omega

#below we are finding omega for the g modes

def omegaG(n, l):
  omega_squared = (-l*(l+1)) / (2*gma1*(n**2))
  omega = sqrt(omega_squared)

  return omega
