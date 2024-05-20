#!/usr/bin/env python3

import argparse
from gendiff.cli import common_parser
from gendiff.generate_diff import generate_diff



def main():
    args = common_parser()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__=='__main__':
    main()
