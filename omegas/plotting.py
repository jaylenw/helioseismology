import matplotlib.pyplot as plt  #importing necessary modules to plot
import numpy as np               #importing numpy to help convert list to array
                                 #to obtain imaginary portion of the list
                                 #look at plotomegaG fxn


# Matplotlib can not plot in interactive mode.  Only when running a .py file.

""" Pulling in data such as the lists from main.py to here and then
display the graph/plot/spectrum """

def plotomegaP(l_list, omegaP_list):

  plt.title("Angular Degrees vs. Omega P Modes")
  plt.grid(True) #just adding a dotted grid for fun
  plt.plot(l_list, omegaP_list, 'bo') #l_list is x-axis, omegaP_list is y-axis)
  #the 'bo' just means don't use default line plot, but use blue filled circles

  plt.xlabel('Angular Degrees') #labeled the axis
  plt.ylabel('Omegas')          #labeled the axis
  plt.show()

  return

def plotomegaGsqrd(l_list, omegaGsqrd_list):

  plt.title("Angular Degrees vs. Omega G squared Modes")
  plt.grid(True) #just adding a dotted grid for fun
  plt.plot(l_list, omegaGsqrd_list, 'bo')
  #the 'bo' just means don't use default line plot, but use blue filled circles

  plt.xlabel('Angular Degrees') #labeled the axis
  plt.ylabel('Omega Squares')          #labeled the axis
  plt.show()

  return

def plotomegaG(l_list, omegaG_list):

  """Below taking necessary process to convert the list to array.  Numpy allows
  you to pull imaginary components from arrays. I'm converting the list that has
  imaginary list to an array.  Then acting on the array to pull the numbers from
  the imaginary components so that matplotlib can successfully graph it"""

  omegaG_array = np.array(omegaG_list)  #converting list to new array
  omegaG_array = omegaG_array.imag      #returning imaginary components without
                                        #the imaginary type. ie. convert to float

  plt.title("Angular Degrees vs. Omega G Modes")
  plt.grid(True) #just adding a dotted grid for fun
  plt.plot(l_list, omegaG_array, 'bo')
  #the 'bo' just means don't use default line plot, but use blue filled circles

  plt.xlabel('Angular Degrees') #labeled the axis
  plt.ylabel('Omegas, in Imaginary Results')          #labeled the axis
  plt.show()

  return
