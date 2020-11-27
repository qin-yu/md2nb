# `md2nb` - Converting Markdown Files to Jupyter Notebook
[![GitHub license](https://img.shields.io/badge/license-BSD%203%20Clause-blue.svg)](https://github.com/qin-yu/ml-julia-boston-housing/blob/master/LICENSE)
[![Julia v1.0.1](https://img.shields.io/badge/Python-v3.x.x-brightgreen.svg)](https://julialang.org/blog/2018/08/one-point-zero)

by [Qin Yu](https://github.com/qin-yu), Nov 2020

## Table of Contents
- [Manifesto](#manifesto)
- [Usage](#usage)

# Manifesto
Taking notes using Markdown makes it easier for sharing on GitHub, but GitHub doesn't display Latex-style mathematics in `.md` files. A good workaround is to write Markdown in Jupyter notebooks and share the `.ipynb` files on GitHub, since everything inside is usually rendered properly. However, it is easier to take notes on a local text editor such as VSCode with Markdown support, becuase it automatically generates and updates the table of content, and you don't have to run a notebook server to take notes.

This package is quite simple. But the author decided to make it a package because of the encouraging [talk](https://www.youtube.com/watch?v=GIF3LaRqgXo) by Mark Smith at EuroPython 2019.

# Usage
`md2nb.py` finds all `.md` files in the current working directory and port them into `.ipynb` files with a single Markdown block.

You can either install it for easy invocation:
```bash
$ python -m pip install md2nb
$ cd <THE FOLDER CONTAINING MARKDOWNS>
$ md2nb
```

Or simply use the single python script:
```bash
$ python md2nb.py
```
