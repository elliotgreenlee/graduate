#!/usr/bin/env python


import argparse
import os


def setup_argparser():

    parser = argparse.ArgumentParser(description='Command line program to put line numbers at the beginning of text files within a directory.')
    requiredArguments = parser.add_argument_group('Required Arguments')
    requiredArguments.add_argument('--i', '--input_directory', dest='input_dir', required=True, type=str, help="Directory of input files that we want to line number.")
    requiredArguments.add_argument('--o', '--output_directory', dest='output_dir', required=True, type=str, help="Directory to save the numbered files to.")
    return parser


def main():
    args = setup_argparser().parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    for dirpath, subdirs, files in os.walk(args.input_dir):
        for filename in files:
            with open(os.path.join(dirpath, filename), 'r') as input_file:
                with open(os.path.join(args.output_dir, filename), 'w') as output_file:
                    line_counter = 0
                    for line in input_file.readlines():
                        output_file.write('{}>>>{}'.format(line_counter, line))
                        line_counter += 1


if __name__ == '__main__':
    main()
