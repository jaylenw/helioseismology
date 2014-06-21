
def float_list(density, holdingtemperaturelist, holdingpressurelist, holdinggamma1list):

  density = float(density)

  for number in xrange(0, len(holdingtemperaturelist) -1):

    holdingtemperaturelist[number] =  float(holdingtemperaturelist[number])
    holdingpressurelist[number] =  float(holdingpressurelist[number])
    holdinggamma1list[number] =  float(holdinggamma1list[number])


  return density, holdingtemperaturelist, holdingpressurelist, holdinggamma1list
