import sys
import glob
import json
import argparse
from chardet.universaldetector import UniversalDetector

__copyright__ = "Copyright 2020, Qin Yu"
__author__ = "Qin Yu"
__email__ = "qin.yu@embl.de"

template = '''{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source":
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}'''


def detect_encoding(file_path):
    detector = UniversalDetector()
    detector.reset()
    with open(file_path, 'rb') as f_md:
        for line in f_md:
            detector.feed(line)
            if detector.done:
                break
        detector.close()

    return detector.result['encoding']


def md2nb(file_path, extension='.md'):
    # `str()` prints strings with single quotes, while `json.dumps()` prints with double quotes.
    with open(file_path, 'r', encoding=detect_encoding(file_path)) as f_md:
        t_md = f_md.readlines()
    t_nb = template[:78] + json.dumps(t_md) + template[78:]
    t_nb = json.loads(t_nb)  # 'load string'
    assert len(extension) > 0  # TODO: use try...catch... here
    with open(file_path[:-len(extension)] + '.ipynb', 'w') as f_nb:
        # Making JSON human readable (aka "pretty printing") is as easy as passing an integer value for the indent parameter
        # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
        json.dump(t_nb, f_nb, indent=2)
    return


def md2nb_all(directory='.', extension='.md'):
    if directory[-1] == '/' and len(directory) > 1:
        directory = directory[:-1]

    file_paths = [
        file_path for file_path
        in glob.glob(f"{directory}/*{extension}")
    ]
    print(f"Converting '{extension}' files within {directory}/:")
    print('\t' + '\n\t'.join(file_paths))
    for file_path in file_paths:
        md2nb(file_path, extension=extension)
    return


def main():
    parser = argparse.ArgumentParser()
    # TODO: Check these are actual file paths
    parser.add_argument("filenames", help="files to be converted", nargs='*')
    # TODO: Check these are actual directory paths
    # TODO: Allow more than one directory
    parser.add_argument(
        "--dir", help="directory containing the Markdown files")
    parser.add_argument(
        "--ext", help="target only files with this filename extension", dest="extension", default='.md')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()

    if args.filenames:
        print(f"Converting the following files:")
        print('\t' + '\n\t'.join(args.filenames))
        for file_path in args.filenames:
            md2nb(file_path)

    if args.dir:
        md2nb_all(directory=args.dir, extension=args.extension)


if __name__ == '__main__':
    main()
