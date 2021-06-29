import os

def shell(out):
    stream = os.popen(out)
    output = stream.read()
    output

shell('sudo rm -rf LCD-show')
shell('git clone https://github.com/goodtft/LCD-show.git')
shell('chmod -R775 LCD-show')
shell('cd LCD-show/')
shell('sudo ./LCD7C-show')