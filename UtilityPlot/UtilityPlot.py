#Tom Diehl 1-16-15
#Takes in 4 csv files with 3 columns formatted
#"mm-dd-yy hr:min:sec , bandwith , latency"
#and plot column 1 vs 2 or 1 vs 3 in sublpots

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates 
import matplotlib.mlab as mlab
from matplotlib.ticker import FuncFormatter
import csv
import datetime

dt = datetime.datetime

#filenames to be read in
file0 = 'TOS_OTC_BG_Nov17_Dec9'         
file1 = 'TOS_OTC_BG_wired_Nov17_Dec9'
file2 = 'TOS_SSG_BG_Nov17_Dec9'
file3 = 'TOS_SSG_BG_wired_Nov21_Dec9'

# Set font for ticks and titles
font = {'family' : 'sans-serif',
        'weight' : 'bold',
        'size'   : 9}

matplotlib.rc('font', **font)

#adjust positioning to accomomdate titles
fig = plt.figure()
fig.subplots_adjust(bottom=0.04)
fig.subplots_adjust(top=0.96)

def readIn(fileName):
	with open('%s.csv' % fileName) as csvfile:
		temp = mlab.csv2rec(csvfile,names = ['date', 'band','lat'])
	return temp


#plotting function(position number, x-axis data, y-axis data,
#						filename,data type, units, y axis scale)
def iPlot(num,xaxi,yaxi,filename,types, units,scale):	
	if num == 1:	
		ax = plt.subplot(4,1,1)
	elif num== 2: 	
		ax = plt.subplot(4,1,2)
	elif num == 3:
		ax = plt.subplot(4,1,3)
	else:
		ax = plt.subplot(4,1,4)
		
#Set  X and Y titles, format ticks, and set Scales
	plt.plot_date(xaxi,yaxi,'-')
	plt.title(filename + "--%s" % types )
	plt.ylabel(" %s  %s " % (types,units))
	plt.ylim(0,scale)
	majorFormatter = matplotlib.dates.DateFormatter('%m-%d %H:%M')
	ax.xaxis.set_major_formatter(majorFormatter)
	

#select bandwidth, latency, or custom set plots
def plot(dataType):
	nameB = "Bandwidth"
	nameL = "Latency"
	unitsB = " (Mbps)"
	unitsL = "(ms)"
	scaleB = 60
	scaleL = 500

	if dataType == '1':
		iPlot(1,out0['date'],out0['lat'],file0,nameL,unitsL,scaleL)
		iPlot(2,out1['date'],out1['lat'],file1,nameL,unitsL,scaleL)
		iPlot(3,out2['date'],out2['lat'],file2,nameL,unitsL,scaleL)
		iPlot(4,out3['date'],out3['lat'],file3,nameL,unitsL,scaleL)

	elif dataType == '2':
		iPlot(1,out0['date'],out0['band'],file0,nameB,unitsB,scaleB)
		iPlot(2,out1['date'],out1['band'],file1,nameB,unitsB,scaleB)
		iPlot(3,out2['date'],out2['band'],file2,nameB,unitsB,scaleB)
		iPlot(4,out3['date'],out3['band'],file3,nameB,unitsB,scaleB)

	elif dataType =='3':
		iPlot(1,out0['date'],out0['lat'],file0,nameL,unitsL,scaleL)
		iPlot(2,out0['date'],out0['band'],file0,nameB,unitsB,scaleB)
		iPlot(3,out1['date'],out1['lat'],file1,nameL,unitsL,scaleL)
		iPlot(4,out1['date'],out1['band'],file1,nameB,unitsB,scaleB)

def main():
	global out0,out1,out2,out3

	print "Choose plot type"
	valid = ['1','2','3']

	while True:
		dataType = raw_input("1 = Latency\n2 = Bandwidth\n3 = Custom : ")
		if dataType in valid:
			break
		else:
			print('Please enter valid choice\n')
	print "Creating plots..."

	out0 = readIn(file0)
	out1 = readIn(file1)
	out2 = readIn(file2)
	out3 = readIn(file3)
	
	plot(dataType)
	plt.show()

main()
