# Shutting_Up_My_IBM
Making my IBM  x3550 M4 quiet - an adventure in sketchy behaviour
After a few months of having my IBM X3550 M4 running on my bedroom desk, I finally decided to do something about it.

Using a decent chunk of https://github.com/trstringer/linux-core-temperature-monitor.git (I have included a submodule in this repo) as well as infomation and (modified) commands provided by https://www.reddit.com/r/homelab/comments/aa3xj7/ibm_systemx_3650_m2_fan_speed_control/ I have designed a systemctl service that runs to keep fan noise *somewhat* bearable.

I give no guarantees on this not blowing up your own server - and for the love of god don't use this in a production envrioment.
 
That aside, the process to using this & how it works:

This works by using ipmitool to write raw values to set a fan speed on the baseboard - check the linked reddit post for more details :) - I have set up a python script to constantlly check the temperatures of
   the system, and if the temperatures are below 55 degrees C then the fans are set to low (not the lowest possible value, as I live in Australia, if you live in a cooler area/fully air conditioned you may be a
  ble to set this lower), if the cpu temps are between 55 and 65 I let the baseboard decide what speed it wants the fans at, and if the cpu(s) are above 65 then the fans go full throttle (a little on the safe s
  ide - you should be able to work out how to change this using the provided links - if you can't, you probably shouldn't be using this :P )

  ```
      git clone https://github.com/Sebagabones/Shutting_Up_My_IBM.git
      cd Shutting_Up_My_IBM
  ```
