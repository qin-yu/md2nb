# `md2nb` - Converting Markdown Files to Jupyter Notebook
[![GitHub license](https://img.shields.io/badge/license-BSD%203Clause-blue.svg)](https://github.com/qin-yu/ml-julia-boston-housing/blob/master/LICENSE)
[![Julia v1.0.1](https://img.shields.io/badge/Python-v3.x.x-brightgreen.svg)](https://julialang.org/blog/2018/08/one-point-zero)

by [Qin Yu](https://github.com/qin-yu), Nov 2020

## Table of Contents
- [Manifesto](#manifesto)
- [Usage](#usage)
- [Reference](#reference)

# Manifesto
Taking notes using Markdown makes it easier for sharing on GitHub, but GitHub doesn't display Latex-style mathematics in `.md` files. A good workaround is to write Markdown in Jupyter notebooks and share the `.ipynb` files on GitHub, since everything inside is usually rendered properly. However, it is easier to take notes on a local text editor such as VSCode with Markdown support, becuase it automatically generates and updates the table of content, and you don't have to run a notebook server to take notes.

# Usage
`md2nb.py` finds all `.md` files in the current working directory and port them into `.ipynb` files with a single Markdown block.
```bash
$ python md2nb.py
```

# Reference
- [How to Publish an Open-Source Python Package to PyPI](https://realpython.com/pypi-publish-python-package/)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
