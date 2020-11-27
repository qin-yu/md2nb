import glob
import json

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


def md2nb(file_path, extension='.md'):
    # `str()` prints strings with single quotes, while `json.dumps()` prints with double quotes.
    with open(file_path, 'r') as f_md:
        t_md = f_md.readlines()
    t_nb = template[:78] + json.dumps(t_md) + template[78:]
    t_nb = json.loads(t_nb)  # 'load string'
    assert len(extension) > 0  # TODO: use try...catch... here
    with open(file_path[:-len(extension)] + '.ipynb', 'w') as f_nb:
        # Making JSON human readable (aka "pretty printing") is as easy as passing an integer value for the indent parameter
        # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
        json.dump(t_nb, f_nb, indent=2)
    return


def md2nb_all(extension='.md'):
    file_paths = [file_path for file_path in glob.glob(f"*{extension}")]
    print(f"The following files are about to be converted: {file_paths}")
    for file_path in file_paths:
        md2nb(file_path, extension=extension)
    return


if __name__ == '__main__':
    md2nb_all()
