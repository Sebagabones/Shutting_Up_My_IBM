# Shutting_Up_My_IBM
Making my IBM  x3550 M4 quiet - an adventure in sketchy behaviour
After a few months of having my IBM X3550 M4 running on my bedroom desk, I finally decided to do something about it.

Using a decent chunk of https://github.com/trstringer/linux-core-temperature-monitor.git (I have included a submodule in this repo) as well as infomation and (modified) commands provided by https://www.reddit.com/r/homelab/comments/aa3xj7/ibm_systemx_3650_m2_fan_speed_control/ I have designed a systemctl service that runs to keep fan noise *somewhat* bearable.

I give no guarantees on this not blowing up your own server - and for the love of god don't use this in a production envrioment.
 
That aside, the process to using this & how it works:

This works by using ipmitool to write raw values to set a fan speed on the baseboard - check the linked reddit post for more details :) - I have set up a python script to constantlly check the temperatures of the system, and if the temperatures are below 55 degrees C then the fans are set to low (not the lowest possible value, as I live in Australia, if you live in a cooler area/fully air conditioned you may be able to set this lower), if the cpu temps are between 55 and 65 I let the baseboard decide what speed it wants the fans at, and if the cpu(s) are above 65 then the fans go full throttle (a little on the safe side - you should be able to work out how to change this using the provided links - if you can't, you probably shouldn't be using this :P )

Now - how to do this yourself - when it comes to the file permissions refer to this for guidance: https://askubuntu.com/questions/155791/how-do-i-sudo-a-command-in-a-script-without-being-asked-for-a-password - I know this is sketchy way of doing it, if you've got a better way to do this please let me know :)

```
    git clone https://github.com/Sebagabones/Shutting_Up_My_IBM.git
    cd Shutting_Up_My_IBM
    sudo chown root:root /fullpath/to/Shutting_Up_My_IBM/quitePowerLevel.sh
    sudo chmod 700 /fullpath/to/Shutting_Up_My_IBM/quitePowerLevel.sh
    sudo chown root:root /fullpath/to/Shutting_Up_My_IBM/middlePowerlevel.sh
    sudo chmod 700 /fullpath/to/Shutting_Up_My_IBM/middlePowerlevel.sh
    sudo chown root:root /fullpath/to/Shutting_Up_My_IBM/fullPowerLevel.sh
    sudo chmod 700 /fullpath/to/Shutting_Up_My_IBM/fullPowerLevel.sh
        
```
    Now run ```sudo visudo```
