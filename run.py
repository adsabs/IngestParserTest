"""
run.py -- parse a publisher metadata record and 
          output an ADS Ingest_Data_model object
"""

import argparse
import json
import os
from adsingestp.parsers.crossref import CrossrefParser
from adsingestp.parsers.jats import JATSParser
from adsingestp.parsers.datacite import DataciteParser
from adsingestp.parsers.elsevier import ElsevierParser

PARSER_TYPES = {'jats': JATSParser(),
                'dc': DataciteParser(),
                'cr': CrossrefParser(),
                'nlm': JATSParser(),
                'elsevier': ElsevierParser()
               }

def get_args():

    parser = argparse.ArgumentParser('Create an ADS record from a DOI')

    parser.add_argument('-f',
                        '--infile',
                        dest='infile',
                        action='store',
                        default=None,
                        help='Path to input metadata file')

    parser.add_argument('-t',
                        '--file_type',
                        dest='file_type',
                        action='store',
                        default=None,
                        help='Type of input file: jats, nlm, dc, cr, elsevier')

    return parser.parse_args()



def main():

    args = get_args()
    if args.infile and args.file_type:
        infile = args.infile
        file_type = args.file_type
        outfile = './' + os.path.basename(infile) + '.json'

        output = None

        try:
            with open(infile,'r') as fin:
                data = fin.read()
        except Exception as err:
            print('Error reading data file: %s' % err)
        else:
            try:
                if file_type == 'nlm':
                    parser = JATSParser()
                    output = parser.parse(data, bsparser='lxml-xml')
                else:
                    parser = PARSER_TYPES.get(file_type, None)
                    if not parser:
                        raise Exception("No such parser: %s" % file_type)
                    output = parser.parse(data)
            except Exception as err:
                print('Error parsing data: %s' % err)
            else:
                if output:
                    with open(outfile,'w') as fj:
                        fj.write(json.dumps(output, indent=2))
                    print('Parsing succeeded.  Results:\n\tParser type: %s\n\tInfile: %s\n\tOutfile: %s' % (file_type, infile, outfile))
                else:
                    print('Parsing failed, no output')
    else:
        print('Parsing failed, you must specify and input file (-f) and a file type (-t)')


if __name__ == '__main__':
    main()
