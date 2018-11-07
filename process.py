# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:31:05 2018

@author: mahmad
"""
import matplotlib.pyplot as plt
import numpy as np
import math
import PlotSpeed as speed
class velocity:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
    def mag(self):
        return math.sqrt(self.x**2 + self.y**2 +self.z**2)
class doppler:
    def __init__(self):
        self.prn = 0
        self.time = 0
        self.pos = 0
        self.velocity = 0
        self.measured = 0
        self.calculated = 0
        self.diff = 0
file = open('range_data.log_doppler')
vel = velocity()
pos = velocity()
dop = doppler()
lines = file.readlines()
dopplers = {i:[] for i in range(40)}
_dops = {i:{} for i in range(40)}
for line in lines[1:]:
    pieces = line.split(' ')
    pieces = [x for x in pieces if x != '']
    dop = doppler()
    dop.time = float(pieces[10])
    dop.measured = float(pieces[2])
    dop.calculated = float(pieces[3])
    dop.prn = int(pieces[0])
    dop.diff = dop.measured - dop.calculated
    dopplers[int(pieces[0])].append(dop)
    _dops[dop.prn][dop.time] = dop
_time,difference = speed.velocities()
dict_time = {_time[x]:difference[x] for x in range(len(_time))}
print("Showing  speed difference")
plt.plot(_time,difference,'b-')
plt.show()
for i in dopplers:
    x = []
    y = []
    z = []
    average = 0
    average2 = 0
    count,pop,_count = 0,0,2
    if dopplers[i] != []:
        dops = dopplers[i]
        for dop in dops:
            count+=1
            average += dop.measured
            average2 += dop.calculated
            if count== _count:
                x.append(dop.time)
                y.append(average/count)
                #print(dop.velocity.mag())
                z.append(average2/count)
                average -= dops[pop].measured
                average2-= dops[pop].calculated
                count-=1
                pop+=1
        dop_diff = [(y[j] - z[j]) for j in range(len(y))]
        los_speed =[3.6*(a - y[index])*(299792458.0)/1575420000 for index, a in enumerate(z)]
        plt.subplot(211)
        plt.title('SAT_' + str(i))
        #print(i, x[0],_time[0],len(x),len(_time))

        d = len(_time) - len(x)
        tm = []
        df = []
        if d > 0:
            for a,b in enumerate(_time):
                if(b>=x[0] and b <= x[-1]):
                    tm.append(b)
                    df.append(difference[a])

        #tdiff = tm[0] - x[0]
        #tm = [z - tdiff for z in tm]
        #print(i, x[0],tm[0],len(x),len(tm))
        plt.plot(x,y,'r-',x,z,'b-')
        plt.xlabel('Time (sec)')
        plt.ylabel('Doppler (Hz)')
        plt.legend(['Measured','Predicted'])
        plt.subplot(212)
        #plt.plot(tm,df,'b-')
        plt.plot(x,dop_diff,'b-')
        plt.xlabel('Time (sec)')
        plt.ylabel('Doppler difference')
        plt.legend(['Doppler difference'])
        plt.savefig('satellite_' + str(i) +'.png')

        plt.close()
        #plt.plot(x,y,'r',x,z,'b')
        #plt.legend(['measured','predicted'])
        #plt.savefig('satellite_' + str(i) +'_abs_' + '.png')
