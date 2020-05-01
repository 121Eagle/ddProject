import math
def sizeParse(N):
    multiples = {'c':1,'w':2,'b':512,'K':1024, 'KB':1000, 'M':1024 ** 2, 'G':1024 ** 3, 'T':1024 ** 4, 'P':1024 ** 5, 'E':1024 ** 6, 'Z':1024 ** 7, 'Y':1024 ** 8,
                 'MB':1000 ** 2, 'GB':1000 ** 3, 'TB':1000 ** 4, 'PB':1000 ** 5, 'EB':1000 ** 6, 'ZB':1000 ** 7, 'YB':1000 ** 8,}
    multiples.update({'x'+x:multiples[x] for x in multiples.keys()})
    try:
        N=int(N)
    except ValueError:
        j = list(multiples.keys())
        j.sort(key=len(),reverse=True)
        for i in j:
            if i in N:
                # This system will multiply the integer value, by the metric function given.
                return (int(N[:-len(i)]) * multiple[i])
        raise ValueError
    except TypeError:
        return N
    else:
        return N
def sparce(data, blocksize):
    if ((lindex := data.find(b'\x00')) > -1):
        data = data[:lindex] + data[lindex:].strip(b'\x00')
    if ((rindex := data.rfind(b'\x00')) > -1):
        data = data[:rindex].rstrip(b'\x00') + data[rindex:]
    length = len(data)
    data = data + in_file.read(size - length)
    return sparce(data,blocksize)

def is_not_number(N):
    return (not isinstance(N, (type(1),type(math.inf),type(0.1),type(math.pi))))

def dd(inputName='', outputName='', blockSize=512, count=math.inf, seek='0', skip='0', conv=None):
    size = sizeParse(blockSize)
    if is_not_number(count):
        count = sizeParse(count)
    with open(inputName,'rb') as in_file:
        in_file.seek(sizeParse(skip)*size,0)
        with open(outputName,'wb') as out_file:
            out_file.seek(sizeParse(seek)*size,0)
            while 0 < count :
                data = in_file.read(size)
                if (conv == 'sparse'):
                    data = sparce(data,size)
                if (conv == 'lcase'):
                    data = data.lower()
                else if (conv == 'ucase'):
                    data = data.upper()
                else:
                    pass
                out_file.write(in_file.read(size))
                count = count - 1
