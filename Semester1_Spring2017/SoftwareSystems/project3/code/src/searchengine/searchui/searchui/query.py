#!/usr/bin/env python

import json
import os
import re
from collections import defaultdict, namedtuple
from itertools import izip_longest


NON_ALPHANUMERIC_CHARS = re.compile('[^a-zA-Z0-9 ]')
index = None


class InvertedIndex(object):

    def __init__(self, index_file, id_to_title_file):
        if not os.path.isfile(index_file):
            print('Inverted Index file does not exist at the path {}, please ensure it does!'.format(index_file))
            return None

        if not os.path.isfile(id_to_title_file):
            print('Page ID to Page Title file does not exist at the path {}, please ensure it does!'.format(index_file))
            return None

        self.index_file = index_file
        self.id_to_title_file = id_to_title_file
        self._id_to_title_mapping = read_id_to_title_mapping(id_to_title_file)
        self._index = read_index(index_file)

    def get_index(self):
        return self._index

    def get_title(self, page_id):
        page_title = self._id_to_title_mapping.get(page_id, None)

        if page_title is None:
            print('Page title does not exist for id {}!'.format(page_id))
            return None

        return page_title

def read_id_to_title_mapping(id_to_title_file):
    with open(id_to_title_file, 'r') as f:
        for line in f.readlines():
            line_split = line.split(',')
            if len(line_split) < 1:
                raise ValueError('ID to Title file is corrupted!')



def setup_index(index_file):
    global index
    index = InvertedIndex(index_file)


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
                    doc_name = doc_name.strip()
                    if i == 0:
                        inverted_index[word] = {doc_name: [(line_number, word_number)]}
                    else:
                        inverted_index[word][doc_name] = [(line_number, word_number)]
            else:
                for doc_name in matched_docs_list:
                    doc_name = doc_name.strip()
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


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


def query(query):

    if index is None:
        raise ValueError('Inverted Index has not yet been created! Please create it first.')

    query = json.loads(query)
    results = index_search(index.get_index(), query["query"])

    if len(results) == 0:
        return None

    dict_results = []
    for result in results:
        dict_results.append({"word": result.word, "doc_name": result.doc_name,
                             "line_number": result.line_number, "word_number": result.word_number})

    return dict_results

