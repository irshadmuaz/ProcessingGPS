
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
speeds = [5,10,15,20,25,30]
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
            s,speed =e.split(':')
            if float(speed) <= limit:
                count+=1
                if s == '1':
                    passes+=1
        #row.append(str(passes) + "/" + str(count))
        row.append(float(passes)/count*100)
    writer.writerow(row)
