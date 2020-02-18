#!env python
import errno
import os
import pprint
import argparse

global args, pp

def main():

    global args, pp
    pp = pprint.PrettyPrinter(indent=4)    

    parser = argparse.ArgumentParser(description='String')
    parser.add_argument('--string', 
            required=False,
            type=str, 
            nargs=1, 
            help='string'
            )


    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
  main()
        