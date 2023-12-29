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
    os.system('sudo /fullpath/to/Shutting_Up_My_IBM/quitePowerLevel.sh')

def hawtAF():
    os.system('sudo /fullpath/to/Shutting_Up_My_IBM/middlePowerlevel.sh')
    time.sleep(20)

def moarPOWER():
    os.system('sudo /fullpath/to/Shutting_Up_My_IBM/fullPowerLevel.sh')
    time.sleep(40)

def main():
    """Main script execution"""
    infiLoop = False;
    check = 0
    while infiLoop != True:
        rsd = raw_sensor_data()
        core_temps = parse_core_temps(rsd)
        time.sleep(0.05)
        toggle = 0
        for x in core_temps:
            if(int(core_temps[x]) > 55):
                hawtAF()
                toggle = 1
            if(int(core_temps[x]) > 65):
                moarPOWER()
                toggle = 1
        if(toggle == 0):
                tellCpuToShutUp()

if __name__ == '__main__':
    main()
