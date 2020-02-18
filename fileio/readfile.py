#!env python
import errno
import os
import pprint
import argparse

global args, pp

def main():

    global args, pp
    pp = pprint.PrettyPrinter(indent=4)    

    parser = argparse.ArgumentParser(description='Filename')
    parser.add_argument('--file', 
            required=True,
            type=str, 
            nargs=1, 
            help='string'
            )
    parser.add_argument('--tab', 
            required=False,
            action='store_true',
            )

    args = parser.parse_args()
    print(args)
    with open(args.file[0], "r") as infile:
        for line in infile:
            if args.tab:
                print ( "---> ", line.rstrip().split("\t" ) )
            else:
                print ( "---> " + line.rstrip() )

if __name__ == "__main__":
  main()
        


