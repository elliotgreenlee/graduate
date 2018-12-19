#!/usr/bin/env python


import argparse
import logging
import os
import re
import sys
from collections import defaultdict, namedtuple


NON_ALPHANUMERIC_CHARS = re.compile('[^a-zA-Z0-9 ]')


def setup_argparser():

    parser = argparse.ArgumentParser(description='Command line program to query our inverted index.')
    requiredArguments = parser.add_argument_group('Required Arguments')
    requiredArguments.add_argument('--i', '--index', dest='index', required=True, type=str, help="Inverted Index input file.")
    return parser



def read_index(index_file):
    """
        Builds an index of the form:
            {word : { doc_name : [(line_number, word_number), ...] } }

        from an inverted index file with lines structured in the form:
            word,line_number,word_number -> doc_name_1, doc_name_2, ..., doc_name_n
    """

    inverted_index = defaultdict()

    with open(index_file, 'r') as f:
        for line in f.readlines():
            key_val_parts = line.split('->')
            if len(key_val_parts) != 2:
                raise ValueError('The input file is not in the correct format. The key and value of the inverted index must be seperated by a "->" character sequence.')

            word_and_position = key_val_parts[0].rstrip()
            matched_docs = key_val_parts[1].rstrip()
            matched_docs_list = matched_docs.split(', ')

            try:
                word, line_number, word_number = word_and_position.split(',')
            except ValueError:
                raise ValueError('The key is not in the right format. It should be of the format "word,line_number,word_number".')

            word_entry = inverted_index.get(word)
            if word_entry is None:
                for i, doc_name in enumerate(matched_docs_list):
                    if i == 0:
                        inverted_index[word] = {doc_name: [(line_number, word_number)]}
                    else:
                        inverted_index[word][doc_name] = [(line_number, word_number)]
            else:
                for doc_name in matched_docs_list:
                    doc_entry = word_entry.get(doc_name)
                    if doc_entry is None:
                        word_entry[doc_name] = [(line_number, word_number)]
                    else:
                        doc_entry.append((line_number, word_number))

    return inverted_index



def index_search(inverted_index, query):
    """
        Takes the in-memory inverted index generated earlier and a
        query string of one or more words, and returns a result of the form:
            [(doc_name, line_number, word_number), ...]
    """

    QueryResult = namedtuple('QueryResult', 'word doc_name line_number word_number')

    results = []
    cleaned_query = re.sub(NON_ALPHANUMERIC_CHARS, '', query.rstrip())
    words_in_query = cleaned_query.lower().split(' ')

    for word in words_in_query:
        word_entry = inverted_index.get(word)
        if word_entry is not None:
            for doc_name, word_positions in word_entry.items():
                for line_number, word_number in word_positions:
                    results.append(QueryResult(word, doc_name, line_number, word_number))

    return results



def main():
    logger = logging.getLogger('query_inverted_index')

    args = setup_argparser().parse_args()

    if not os.path.isfile(args.index):
        print('Inverted Index file does not exist at the path {}, please ensure it does!'.format(args.index))
        sys.exit(1)

    print('Building inverted index in memory...')
    inverted_index = read_index(args.index)
    print('Finished building inverted index in memory.')

    query = raw_input('Please enter your query: ')
    results = index_search(inverted_index, query)

    if len(results) == 0:
        print('Your query returned no results!')
    else:
        print('Results: ')
        for i, result in enumerate(results):
            print('\tWord: {:>29}\n\tDocument Name: {:>20}\n\tLine Number: {:>22}\n\tWord Position on Line: {:>12}'.format(
                result.word, result.doc_name, result.line_number, result.word_number))
            if i != len(results) - 1:
                print('')



if __name__ == '__main__':
    main()
