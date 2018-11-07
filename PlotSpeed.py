import sys
import re
import math
import matplotlib.pyplot as plt
import collections
if len(sys.argv) < 3:
    print('USAGE: <Real> <spoofed>')
    exit(-1)
def extract(filename):
    lines = open(filename,'r').readlines()
    velocity = []
    times = []
    for line in lines[1:]:
        #match = re.search(r'\s+(-?\d+\.?\d+?)\s+(-?\d+\.?\d+?)\s+(-?\d+\.?\d+?)\s+(-?\d+\.?\d+?)\s+(\d+)',line,re.I|re.M)
        match = re.search(r'\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)',line,re.I|re.M)
        if match:
            data = match.groups()
            sum = 0
            for v in data[:-2]:
                sum+=(float(v))**2
            vel = math.sqrt(sum)
            time = int(data[-1])
            velocity.append(vel*3.6)
            times.append(time)
    print('len of ' + filename + ' ' + str(len(velocity)))
    return velocity,times
def velocities():
    vel,t = extract(sys.argv[1])
    vel2,t2 = extract(sys.argv[2])
    

    #spoofed_velocity = []
    #actual_velocity = []
    t_actual = []
    diff= t[0] - t2[0]
    """trim_index = 0
    while vel2[trim_index] == 0:
        trim_index+=1
    t2 = t2[trim_index:]
    t = t[trim_index:]
    actual_velocity = vel[trim_index:]
    spoofed_velocity = vel2[trim_index:]
    t_actual = t2
    #print(len(spoofed_velocity),len(actual_velocity))
    print('velocities',len(vel),len(vel2),t[-1] - t[0] ,t[1] - t2[1], t[0] - t2[0])"""
    if len(vel2) < len(vel):
        vel = vel[(len(vel) - len(vel2)):]
        t = t[(len(t) - len(t2)):]
    elif len(vel) < len(vel2):
        vel2 = vel2[(len(vel2) - len(vel)):]
        t2 = t2[(len(t2) - len(t)):]
    #print('extracted_speeds', len(actual_velocity),len(spoofed_velocity))
    actual_velocity = vel
    spoofed_velocity = vel2
    plt.plot(t2,actual_velocity,'r-',t2,spoofed_velocity,'b-')
    difference = [(spoofed_velocity[i] - actual_velocity[i]) for i in range(len(actual_velocity))]
    # print(difference)
    # plt.plot(t_actual,difference,'b-')
    # plt.xlabel('Time(sec)')
    # plt.ylabel('Velocity (kmph)')
    #plt.legend(['actual speed','spoofer_speed'])
    plt.legend(['speed difference'])
    plt.show()
    return t2,difference
