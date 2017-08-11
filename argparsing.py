#!/usr/bin/python3

import argparse



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Application description.')

    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')

    parser.add_argument('-s', '--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()

    print(args)

    print(args.accumulate(args.integers))
