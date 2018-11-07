
import sys,csv
import re
import math
import matplotlib.pyplot as plt
import collections
import pandas as pd
if len(sys.argv) < 2:
    print('USAGE: <csv-file>')
    exit(-1)
file = sys.argv[1]
speeds = [x for x in range(30)]
output = open('status.csv','wb')
writer = csv.writer(output,delimiter=',')

data = pd.read_csv(file,header=None)

thresholds = data.loc[0,:]
cols = len(thresholds)
writer.writerow(thresholds)
row = []
for limit in speeds:
    row = []
    row.append(limit)
    for c in range(1,cols-1):
        count=0
        passes = 0
        for e in data.loc[1:,c]:
            s,mean,mode,speed =e.split(':')
            #s,speed = e.split(':')
            #if math.floor(float(speed)) == math.floor(limit):
	    #if float(speed) <= limit:
	    if float(speed) > limit-1 and float(speed) <= limit:
                count+=1
                if mode == '1':
                    passes+=1
                if float(speed) > 10 and c < 15 and mode == '0':
                    print(e,c,data.loc[0,c])
        #row.append(str(passes) + "/" + str(count))
	if count > 0:
        	row.append(str(float(passes)/count*100)+ ' : ' + str(passes) + "/" + str(count))
    writer.writerow(row)
