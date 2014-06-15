massSun = 1.989*10**30 #mass of Sun in kilograms
gravC = 6.67384*10**(-11)

def density(r):

  rho = (massSun)/((4.0/3)/((pi)*(r**3))) #density equation

  return rho

def pressure(r):

  p = (gravC*(massSun**2)) / (4*pi*(r**4)) #pressure equation

  return p
