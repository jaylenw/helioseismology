import matplotlib.pyplot as plt


# Matplotlib can not plot in interactive mode.  Only when running a .py file.

""" I am going to see if I can pull in data from main.py to here and then
display the graph/plot/spectrum """

def plotomegaP(l_list, omegaP_list):

  plt.plot(l_list, omegaP_list)
  #plt.ylablel('Omega P Values')
  plt.show()

  return


def plotomegaG(l_list, omegaG_list):

  plt.plot(l_list, omegaG_list)
  #plt.ylabel("Omega G Values")
  plt.show()

  return
