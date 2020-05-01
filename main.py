import argparse # don't remove me
from os import path
from dd import dd

if __name__ == "__main__": # don't remove this line

    p = argparse.ArgumentParser() # don't remove this line either

    ### EDIT THESE AS NEEDED ###
    p.add_argument("input", type=str, action="store", metavar='if=', help="read from file")
    p.add_argument("output", type=str, action="store", metavar='of=', help="write to file")
    p.add_argument("blocksize", type=str, nargs='?', action="store", metavar='bs=', help="blocksize", default='bs=512')
    p.add_argument("count", type=int, required=False, nargs='?', action='store', metavar='count=')
    p.add_argument('conv', type=str, action='store', metavar='conv=', choices=('ucase','lcase','sparce'))
    ############################

    args = p.parse_args()

    ### YOUR LOGIC BELOW ###
    variables = vars(args)
    variables.update({x:variables[x].split('=')[1] for x in variables.keys()})
    print(variables)

    if (path.exists(args.input) and path.exists(args.output)):
        if (not path.isfile(args.input)) and (not path.isfile(args.input)):
            raise Exception("Given path is not a file!")
    else:
        raise Exception("Given path does not exist!")
    dd(**variables)
