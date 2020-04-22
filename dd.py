import glob
import os.path
import math

def sizeParse(N):
    multiples = {'c':1,'w':2,'b':512,'KB':1000,'K':1024}
    number,multiple = None
    if(not math.isnan(N)):
        return N
    else if (not math.isnan(N[-2])):
        number,multiple = int(N[:-1]),N[-1]
    else:
        number,multiple = int(N[:-2]),N[-2:]
    return number * multiples[multiple]

def dd(inputName='', outputName='', blockSize=512, count=math.inf, seek=0, skip=0):
    with open(inputName,'rb') as in_file:
        in_file.seek(sizeParse(skip)*sizeParse(blockSize),0)
        with open(outputName,'wb') as out_file:
            out_file.seek(seek,0)
            pass
