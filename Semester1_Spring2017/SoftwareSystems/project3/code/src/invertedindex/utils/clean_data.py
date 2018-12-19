#!/usr/bin/env python

import os
import sys
import json


usage_string = 'clean_data.py INPUT_DIR <OUTPUT_DIR>'


def main():

    output_dir = 'cleaned_pages'

    if len(sys.argv) < 2:
        print(usage_string)
        exit(1)

    if len(sys.argv) == 3:
        output_dir = sys.argv[2]

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    for root, dirs, files in os.walk(sys.argv[1]):
        for filename in files:
            if filename.startswith('wiki'):
                path_to_file = os.path.join(root, filename)
                with open(path_to_file, 'r') as input_file:
                    for line in input_file.readlines():
                        page_entry = json.loads(str(line.strip()))

                        page_title = page_entry.get('title', None)
                        if page_title is None:
                            print('Malformed JSON line in file {}, skipping line!'.format(path_to_file))
                            continue

                        page_title = page_title.replace('/', '-')

                        page_text = page_entry.get('text', None)
                        if page_text is None:
                            print('Malformed JSON line in file {}, skipping line!'.format(path_to_file))
                            continue

                        path_to_output_file = os.path.join(output_dir, page_title)
                        with open(path_to_output_file, 'w') as output_file:
                            for page_line in page_text.split('\n'):
                                output_file.write(page_line.encode("ascii", "ignore"))
                                output_file.write('\n')


if __name__ == '__main__':
    main()