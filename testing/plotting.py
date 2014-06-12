import matplotlib.pyplot as plt


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


def plotomegaG(l_list, omegaG_list):

  plt.title("Angular Degrees vs. Omega G Modes")
  plt.grid(True) #just adding a dotted grid for fun
  plt.plot(l_list, omegaG_list, 'bo')
  #the 'bo' just means don't use default line plot, but use blue filledc circles

  plt.xlabel('Angular Degrees') #labeled the axis
  plt.ylabel('Omegas')          #labeled the axis
  plt.show()                    

  return
