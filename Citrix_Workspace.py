import urllib.request
import os

lines = ["deb http://raspbian.raspberrypi.org/raspbian/ stretch main contrib non-free rpi", "# Uncomment line below then 'apt-get update' to enable 'apt-get source'", "#deb-src http://raspbian.raspberrypi.org/raspbian/ buster main contrib non-free rpi"]

stream = os.popen('sudo rm /etc/apt/sources.list')
output = stream.read()
output

f= open("/etc/apt/sources.list","w+")
for line in lines:
    f.write(line)
    f.write('\n')

urllib.request.urlretrieve("http://downloads.citrix.com/19702/icaclient_21.6.0.28_armhf.deb?__gda__=1624962613_4ed7491a4195aa43e7b6b99037bdc171", "/home/pi/Downloads/Citrix.deb")   

stream = os.popen('sudo dpkg -i /home/pi/Downloads/Citrix.deb')
output = stream.read()
output

stream = os.popen('sudo rm /etc/apt/sources.list')
output = stream.read()
output

lines = ["deb http://raspbian.raspberrypi.org/raspbian/ buster main contrib non-free rpi", "# Uncomment line below then 'apt-get update' to enable 'apt-get source'", "#deb-src http://raspbian.raspberrypi.org/raspbian/ buster main contrib non-free rpi"]
f= open("/etc/apt/sources.list","w+")
for line in lines:
    f.write(line)
    f.write('\n')