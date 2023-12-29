# Shutting_Up_My_IBM
Making my IBM  x3550 M4 quiet - an adventure in sketchy behaviour

After a few months of having my IBM X3550 M4 running on my bedroom desk, I finally decided to do something about it.

Using a decent chunk of https://github.com/trstringer/linux-core-temperature-monitor.git (I have included a submodule in this repo) as well as infomation and (modified) commands provided by https://www.reddit.com/r/homelab/comments/aa3xj7/ibm_systemx_3650_m2_fan_speed_control/ I have designed a systemctl service that runs to keep fan noise *somewhat* bearable.

I give no guarantees on this not blowing up your own server - and for the love of god don't use this in a production envrioment.
 
That aside, the process to using this & how it works:

This works by using ipmitool to write raw values to set a fan speed on the baseboard (a good way to see if this will even work for your system is to try running `  sudo ipmitool raw 0x3a 0x07 0x01 0xff 0x00 && sudo ipmitool raw 0x3a 0x07 0x02 0xff 0x00` and listening for if your fans go crazy (to calm them down run `sudo ipmitool raw 0x3a 0x07 0x01 0xff 0x01 && sudo ipmitool raw 0x3a 0x07 0x02 0xff 0x01`) - check the linked reddit post for more details :) - I have set up a python script to constantlly check the temperatures of the system, and if the temperatures are below 55 degrees C then the fans are set to low (not the lowest possible value, as I live in Australia, if you live in a cooler area/fully air conditioned you may be able to set this lower), if the cpu temps are between 55 and 65 I let the baseboard decide what speed it wants the fans at, and if the cpu(s) are above 65 then the fans go full throttle (a little on the safe side - you should be able to work out how to change this using the provided links - if you can't, you probably shouldn't be using this :P )

Now - how to do this yourself - when it comes to the file permissions refer to this for guidance: https://askubuntu.com/questions/155791/how-do-i-sudo-a-command-in-a-script-without-being-asked-for-a-password - I know this is sketchy way of doing it, if you've got a better way to do this please let me know :)

```
    git clone https://github.com/Sebagabones/Shutting_Up_My_IBM.git
    cd Shutting_Up_My_IBM
    sudo chown root:root /fullpath/to/Shutting_Up_My_IBM/quietPowerLevel.sh
    sudo chmod 700 /fullpath/to/Shutting_Up_My_IBM/quietPowerLevel.sh
    sudo chown root:root /fullpath/to/Shutting_Up_My_IBM/middlePowerlevel.sh
    sudo chmod 700 /fullpath/to/Shutting_Up_My_IBM/middlePowerlevel.sh
    sudo chown root:root /fullpath/to/Shutting_Up_My_IBM/fullPowerLevel.sh
    sudo chmod 700 /fullpath/to/Shutting_Up_My_IBM/fullPowerLevel.sh
        
```

Now run `sudo visudo` and under `%sudo   ALL=(ALL:ALL) ALL` (you may need to add this if it isn't there - I *think* that's what I did) you add:
```
username ALL=(ALL) NOPASSWD: /fullpath/to/Shutting_Up_My_IBM/quietPowerLevel.sh
username ALL=(ALL) NOPASSWD: /fullpath/to/Shutting_Up_My_IBM/middlePowerlevel.sh
username ALL=(ALL) NOPASSWD: /fullpath/to/Shutting_Up_My_IBM/fullPowerLevel.sh
```
Next, change the paths in tempChecking.py to the full paths to the directory where all of this is taking place (lines 27, 30, & 34).

Sweet, now to add this all as a systemctl service (I followed this guide https://www.codementor.io/@ufuksfk/how-to-run-a-python-script-in-linux-with-systemd-1nh2x3hi0e) - add `fanSpeed.service` to `/lib/systemd/system/` making sure to change the path in `fanSpeed.service` to the full path where the directory where `tempChecking.py` is.
Now run:
```
    sudo chmod 644 /lib/systemd/system/fanSpeed.service
    sudo systemctl daemon-reload
    sudo systemctl enable fanSpeed.service && sudo systemctl start fanSpeed.service
```

Check to see if this work by running `sudo systemctl status fanSpeed.service`

And that should *hopefully* be it! Good luck! 

