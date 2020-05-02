import sys # don't remove me
from dd import dd

args = sys.argv
# set all options to null for the start
j={}

for arg in args:
    ##loop through each argument to the tool, and parse the option
    start = lambda string: arg.startswith(string+'=')
    options = ['if','of','bs','count','skip','seek','conv']
    ##I was lazy and put every option as an array
    if start(options[0]):
        inFile = arg[len(options[0]+'='):]
    if start(options[1]):
        outFile = arg[len(options[1]+'='):]
    if start(options[2]):
        j.update({'blockSize':arg[len(options[2]+'='):]})
    if start(options[3]):
        countNum = arg[len(options[3]+'='):]
        j.update({'count':arg[len(options[3]+'='):]})
    if start(options[4]):
        j.update({'skip':arg[len(options[4]+'='):]})
    if start(options[5]):
        j.update({options[5]:arg[len(options[5]+'='):]})
    if start(options[6]):
        j.update({options[5]:arg[len(options[5]+'='):].split(',')})
dd(inFile,outFile,**j)
