import sys
import os
from collections import defaultdict

""" Reference: Stop words source: https://www.ranks.nl/stopwords """

MATCHING_THRESHOLD = 70      # expressed as percentage [0-100]
STOP_WORDS_FILE = "stop_words.txt"


def loadFile(filename):
    with open(filename,'r') as file:
        return file.readlines()


def compare(file_a_data,file_b_data):
    if file_a_data == file_b_data:         # explicit equality check
        print(f"Documents are identical, return code = 1")
        return 1

    stop_words = []
    try:
        with open(STOP_WORDS_FILE) as file:    # ignore comparison from this list
            for line in file:
                stop_words.append(line.rstrip())
    except Exception as e:
        print(f"Encoutered error loading stopwords (none will be used): {e}")

    file_a_text = file_a_data[0].split()    # convert into list of words
    file_b_text = file_b_data[0].split()

    a_dict = {}
    a_dict = defaultdict(lambda: 0, a_dict) # init to 0's

    b_dict = {}
    b_dict = defaultdict(lambda: 0, a_dict)

    for i in file_a_text:                   # load words into dictionary
        if i.lower() not in stop_words:     # stop words source is in lowercase
            a_dict[i] += 1

    for i in file_b_text:
        if i.lower() not in stop_words:
            b_dict[i] += 1

    # compare if keys in a_dict are in b_dict
    intersection_value = set(a_dict.keys()).intersection(set(b_dict.keys()))

    if not bool(intersection_value):                # not a single word in common
        print("Documents don’t have any words in common, return code = 0")
        return 0
    elif a_dict == b_dict:                          # keys and values are identical
        print("Documents have all words, order ignored, with word occurance match exactly, return code = 1")
        return 1
    else:
        ''' Similarity algorithm: two files are similar, if:
            1. Word intersection appears MATCHING_THRESHOLD % of time, and,
            2. Count for a given word is either identical or is expressed as
             percentage of MATCHING_THRESHOLD, i.e.: a/b or b/c > MATCHING_THRESHOLD
        '''
        matching_records = 0
        highest_dict_length = max(len(a_dict),len(b_dict))

        for i in intersection_value:
            if a_dict[i] == b_dict[i]:
                matching_records += 1
            elif a_dict[i] > b_dict[i]:
                if (a_dict[i] / b_dict[i] * 100) > MATCHING_THRESHOLD:
                    matching_records += 1
            else:
                if (b_dict[i] / a_dict[i] * 100) > MATCHING_THRESHOLD:
                    matching_records += 1

        matching_percentage = round(matching_records / highest_dict_length * 100, 2)
        if matching_percentage > MATCHING_THRESHOLD:
            print(f"Documents similarity threshold {matching_percentage}% was above {MATCHING_THRESHOLD}% minimum, i.e.: {matching_records} out of {highest_dict_length} matched, return code = 1")
            return 1
        else:
            print(f"Documents similarity threshold {matching_percentage}% was below {MATCHING_THRESHOLD}% minimum i.e only {matching_records} out of {highest_dict_length}, no match, return code = 0")
            return 0


if __name__ == "__main__":

    if len(sys.argv) is not 3:
        print(f"Please specify two filenames to compare as arguments, for example:\n\n\t"\
            f"{sys.argv[0]} file_one file_two")
        quit()

    if (not os.path.isfile(sys.argv[1])) or (not os.path.isfile(sys.argv[2])):
        print(f"Error, one or more specified file(s) do not exist")
        quit()

    file_a_data = loadFile(sys.argv[1])
    file_b_data = loadFile(sys.argv[2])

    result = compare(file_a_data,file_b_data)

    if result == 0:
        sys.exit(0)
    elif result == 1:
        sys.exit(1)
    else:
        sys.exit(-1)
