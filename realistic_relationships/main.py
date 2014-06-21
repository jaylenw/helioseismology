
#Original text file was called EOS5_00z8x.yxt
datafile = open("EOS5.txt", "r") #opening file

datalist = []
densitylist = []
temperaturelist = []
pressurelist = []
gamma1list = []
linebreakerlist = []
i = 0 #using i to keep track of number of lines

for aline in datafile:
  datalist = aline.split()
  i+=1  #our variable i tracking what line we are on

  """ getting every line in the file and wherever
  there is a white space, it makes it a new element in the list.  Hopefully
  I can use this list to do data manipulation by calling index numbers of each
  line"""

  if len(datalist) == 8:

    densitylist.append(datalist[5])

  if len(datalist) == 12:

    if datalist[0] != "T6":

      temperaturelist.append(datalist[0])
      pressurelist.append(datalist[3])
      gamma1list.append(datalist[10])

    if datalist[0] == "200.000000":
      linebreakerlist.append(i)



#for number in xrange(0, len(densitylist)):
#  print densitylist[number]

#for number in xrange(0, len(temperaturelist)):
#  print temperaturelist[number], "\n", pressurelist[number],"\n", gamma1list[number]

print "Total number of lines is ", i

print len(linebreakerlist)

#for number in xrange(0, len(linebreakerlist)):

#  print linebreakerlist[number]
for n in xrange(0,168):  #total numbers in linebreaker list is 169

  s = linebreakerlist[n]
  t = linebreakerlist[n+1]
  #seven line space between each density set
#for counter in xrange(s, t-7 ):
  #computation happens


datafile.close() #closing the file
