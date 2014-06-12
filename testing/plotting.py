import matplotlib.pyplot as plt


# Matplotlib can not plot in interactive mode.  Only when running a .py file.

""" I am going to see if I can pull in data from main.py to here and then
display the graph/plot/spectrum """

def plotomegaP(omegaP_list):
  x = [1, 2, 3, 4, 5, 6]
  y = omegaP_list
  labels = ['Omega P']

  plt.plot(x, y,)

  plt.show()

  return


def plotomegaG(omegaG_list):
  x = [1, 2, 3, 4, 5, 6]
  y = omegaG_list
  labels = ['Omega G']

  plt.plot(x, y)

  plt.show()

  return
