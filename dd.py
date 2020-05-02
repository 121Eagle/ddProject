from math import inf
import sys
from numbers import Number

multiples = {'c':1,'w':2,'b':512,'K':1024, 'KB':1000, 'M':1024 ** 2, 'G':1024 ** 3, 'T':1024 ** 4, 'P':1024 ** 5, 'E':1024 ** 6, 'Z':1024 ** 7, 'Y':1024 ** 8,
                 'MB':1000 ** 2, 'GB':1000 ** 3, 'TB':1000 ** 4, 'PB':1000 ** 5, 'EB':1000 ** 6, 'ZB':1000 ** 7, 'YB':1000 ** 8,}
multiples.update({'x'+x:multiples[x] for x in multiples.keys()})
multiples.update({x.lower():multiples[x] for x in multiples.keys()})

def sizeParse(N):
    if(isinstance(N,type(''))):
        try:
            N=int(N)
        except ValueError:
            j = list(multiples.keys())
            j.sort(key=len,reverse=True)
            for i in j:
                if i in N:
                    # This system will multiply the integer value, by the metric function given.
                    return (int(N[:-len(i)]) * multiples[i])
            raise ValueError
    if (isinstance(N,Number)):
        return N

def sparce(data, blocksize):
    pass

def is_not_number(N):
    return (not isinstance(N, Number))

def dd(inputName, outputName, blockSize=512, count=inf, seek=0, skip=0, conv=[]):
    size = sizeParse(blockSize)
    if is_not_number(count):
        count = sizeParse(count)
    with open(inputName,'rb') as in_file:
        in_file.seek(sizeParse(skip)*size,0)
        with open(outputName,'wb') as out_file:
            out_file.seek(sizeParse(seek)*size,0)
            while (count > 0) :
                data = in_file.read(size)
                if (conv == 'sparse'):
                    data = sparce(data,size)
                if (conv == 'lcase'):
                    data = data.lower()
                else:
                    if (conv == 'ucase'):
                        data = data.upper()
                out_file.write(data)
                count -= 1
                print(count)
                if(data == None):
                    break
                    count = 0
                    break
            print("That\'s all folks!",file=sys.stderr)
