import matplotlib.pyplot as plt  #importing necessary modules to plot

# Matplotlib can not plot in interactive mode.  Only when running a .py file.

def plotr_rho(radius_list, rho_list):

  plt.title("Radius vs. Rho")
  plt.grid(True) #just adding a dotted grid for fun
  plt.plot(radius_list, rho_list, 'bo') #radius_list is x-axis, density_list is y-axis)

  #the 'bo' just means don't use default line plot, but use blue filled circles

  plt.xlabel('Radius in meters') #labeled the x-axis
  plt.ylabel('Rho in kg/(meters cubed)')          #labeled the y-axis
  plt.show()

  return

def plotr_p(radius_list, pressure_list):

  plt.title("Radius vs. P")
  plt.grid(True) #just adding a dotted grid for fun
  plt.plot(radius_list, pressure_list, 'bo') #radius_list is x-axis, density_list is y-axis)

  #the 'bo' just means don't use default line plot, but use blue filled circles

  plt.xlabel('Radius in meters') #labeled the x-axis
  plt.ylabel('Pressure in N/(meters squared)')          #labeled the y-axis
  plt.show()

  return


def plotp_rho(pressure_list, rho_list):

  plt.title("P vs. Rho")
  plt.grid(True) #just adding a dotted grid for fun
  plt.plot(pressure_list, rho_list, 'bo') #radius_list is x-axis, density_list is y-axis)

  #the 'bo' just means don't use default line plot, but use blue filled circles

  plt.xlabel('Pressure in N/(meters squared)') #labeled the x-axis
  plt.ylabel('Rho in kg/(meters cubed)')          #labeled the y-axis
  plt.show()

  return
