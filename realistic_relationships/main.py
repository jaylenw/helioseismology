
#Original text file was called EOS5_00z8x.yxt
datafile = open("EOS5.txt", "r")

datalist = []
densitylist = []
temperaturelist = []

for aline in datafile:
  datalist = aline.split()


  """ getting every line in the file and wherever
  there is a white space, it makes it a new element in the list.  Hopefully
  I can use this list to do data manipulation by calling index numbers of each
  line"""

  if len(datalist) == 8:

    densitylist.append(datalist[5])

    print "go"

  if len(datalist) == 12:
    print "hi"

    if datalist[0] != "T6":

      temperaturelist.append(datalist[0])

for number in xrange(0, len(densitylist)):
  print densitylist[number]

for number in xrange(0, len(temperaturelist)):
  print temperaturelist[number]
