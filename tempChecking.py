#!/usr/bin/env python3
## BORROWED FROM  https://github.com/trstringer/linux-core-temperature-monitor/tree/master
"""Collect and display relevant hardware temp and load information"""

import csv
from datetime import datetime
import os
import re
import time
import subprocess

def raw_sensor_data():
    """Read the hardware temperature"""

    result = subprocess.run(['sensors'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def parse_core_temps(sensor_data):
    """Extract core temps from sensor data"""

    return {
        i.group(1).replace(' ', '').lower():float(i.group(2))
        for i in re.finditer(r'(Core \d):\s+ \+(\d+\.\d)', sensor_data)
    }

def tellCpuToShutUp():
#    bob = subprocess.run(['sudo ipmitool raw 0x3a 0x07 0x02 0x00 0x01'], stdout=subprocess.PIPE)
#    time.sleep(15)
    os.system('sudo /home/bonesy/Storage/mess/cpuTemps/shutUp2.sh')
#    return(0)

def hawtAF():
    os.system('sudo /home/bonesy/Storage/mess/cpuTemps/HAWT.sh')
    time.sleep(20)
#    return(0)
def moarPOWER():
    os.system('sudo /home/bonesy/Storage/mess/cpuTemps/moarPower.sh')
    time.sleep(40)
def main():
    """Main script execution"""
    bob = False;
    check = 0
    while bob != True:
        rsd = raw_sensor_data()
    #    print(rsd)
        core_temps = parse_core_temps(rsd)
#        for x in core_temps:
#    	    print(core_temps[x])
        time.sleep(0.05)
        toggle = 0
        for x in core_temps:
            if(int(core_temps[x]) > 55):
                hawtAF()
                toggle = 1
            if(int(core_temps[x]) > 65):
                moarPOWER()
                toggle = 1
#                print("over 45")
    #                exit(1)
        if(toggle == 0):
##            print("under 45")
#            time.sleep(20)
##            print("sleeping, and check is")
##            print(check)
#            if(check == 0):
#                check = 2
#            if(check == 1):
                tellCpuToShutUp()
#                check = 0
#            if(check == 2):
#                check = 1
#    exit(0)

if __name__ == '__main__':
    main()
