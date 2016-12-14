# /usr/bin/python
import os
import csv
import json

def generate_pylib(data_dict):
    content = '''"""This file is auto generated"""

class AATTerm(object):

    data_dict = ''' + json.dumps(data_dict) + '''

    @staticmethod
    def get_aat_term(museum, classification_term):
        return AATTerm.data_dict[museum][classification_term]['aat_term']

    @staticmethod
    def get_aat_uri(museum, classification_term):
        return AATTerm.data_dict[museum][classification_term]['aat_uri']
'''
    return content


if __name__ == '__main__':
    # the file in dir_path should named as "museum name + space + whatever + .csv"
    # the content before first space will be treated as museum name
    dir_path = './cleaned_data'
    output_file = 'aat_term.py'

    data_dict = {}

    for name in os.listdir(dir_path):
        if name.endswith('.csv'):
            museum = name.split(' ')[0].lower()
            if not museum in data_dict:
                data_dict[museum] = {}
            with open(os.path.join(dir_path, name), 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                line_count = 0
                for row in reader:
                    line_count += 1
                    if line_count == 1:
                        continue
                    row_dict = {'aat_term': row[1], 'aat_uri': row[2]}
                    data_dict[museum][row[0]] = row_dict

    with open(output_file, 'w') as f:
        f.write(generate_pylib(data_dict))


