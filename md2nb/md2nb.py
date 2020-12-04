import os
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


def is_file(string):
    if not os.path.isfile(string):
        msg = "%r is not a valid file path" % string
        raise argparse.ArgumentTypeError(msg)
    else:
        return string


def is_dir(string):
    if not os.path.isdir(string):
        msg = "%r is not a valid directory path" % string
        raise argparse.ArgumentTypeError(msg)
    else:
        return string


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


def md2nb(file_path, extension=None):
    if extension is None:
        _, extension = os.path.splitext(file_path)

    # `str()` prints strings with single quotes, while `json.dumps()` prints with double quotes.
    with open(file_path, 'r', encoding=detect_encoding(file_path)) as f_md:
        t_md = f_md.readlines()
    t_nb = template[:78] + json.dumps(t_md) + template[78:]
    t_nb = json.loads(t_nb)  # 'load string'

    file_out_path = file_path + \
        '.ipynb' if extension == '' else file_path[:-len(extension)] + '.ipynb'
    with open(file_out_path, 'w') as f_nb:
        # Making JSON human readable (aka "pretty printing") is as easy as passing an integer value for the indent parameter
        # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
        json.dump(t_nb, f_nb, indent=2)
    return


def md2nb_all(directory='.', extension='.md', recursive=False):
    if directory[-1] == '/' and len(directory) > 1:
        directory = directory[:-1]

    file_paths = glob.glob(f"{directory}/**/*{extension}",
                           recursive=True) if recursive else glob.glob(f"{directory}/*{extension}")
    print(f"Converting '{extension}' files within {directory}/ and all subdirectories:") if recursive else print(
        f"Converting '{extension}' files within {directory}/:")
    print('\t' + '\n\t'.join(file_paths))
    for file_path in file_paths:
        md2nb(file_path, extension=extension)
    return


def file_with_extension_exist(directory='.', extension='.m2n', recursive=False):
    if directory[-1] == '/' and len(directory) > 1:
        directory = directory[:-1]

    file_paths = glob.glob(f"{directory}/**/*{extension}",
                           recursive=True) if recursive else glob.glob(f"{directory}/*{extension}")

    return file_paths != []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames", nargs='*', type=is_file, help="paths for files to be converted")
    parser.add_argument(
        "--dir", nargs='+', type=is_dir, help="directory containing the Markdown files")
    parser.add_argument(
        "--ext", nargs='+', help="target only files ending with these", dest="extension")
    parser.add_argument("-r", "--recursive", action='store_true',
                        help="recursively apply `md2nb` to all subdirectories")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()

    if args.filenames:
        print(f"Converting the following user-specified files:")
        print('\t' + '\n\t'.join(args.filenames))
        for file_path in set(args.filenames):
            md2nb(file_path)

    if args.dir:
        no_m2n_files = True
        if args.extension is None:
            for dir_path in set(args.dir):
                if file_with_extension_exist(directory=dir_path, extension='m2n', recursive=args.recursive):
                    no_m2n_files = False
            if no_m2n_files:
                args.extension = ['.md']
            else:
                args.extension = ['.m2n']
        for dir_path in set(args.dir):
            for file_ext in set(args.extension):
                md2nb_all(directory=dir_path,
                          extension=file_ext, recursive=args.recursive)


if __name__ == '__main__':
    main()
