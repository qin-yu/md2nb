# `md2nb` - Converting Markdown Files to Jupyter Notebook
[![BSD license](https://img.shields.io/badge/license-BSD%203%20Clause-blue.svg)](https://github.com/qin-yu/md2nb/blob/main/LICENSE)
![Python v3.6.0](https://img.shields.io/badge/Python-v3.6.0-brightgreen.svg)

Created by [Qin Yu](https://github.com/qin-yu), Nov 2020 - Nov 2020

## Table of Contents
- [Manifesto](#manifesto)
- [Installation](#installation)
- [Usage](#usage)

# Manifesto
Taking notes using Markdown makes it easier for sharing on GitHub, but GitHub doesn't display Latex-style mathematics in `.md` files. A good workaround is to write Markdown in Jupyter notebooks and share the `.ipynb` files on GitHub, since everything inside is usually rendered properly. However, it is easier to take notes on a local text editor such as VSCode with Markdown support, becuase it automatically generates and updates the table of content, and you don't have to run a notebook server to take notes.

This package is quite simple, all it does it to create a Jupyter notebook and paste the content of one file into a Markdown block in this notebook. But the author decided to make it a package because of the encouraging [talk](https://www.youtube.com/watch?v=GIF3LaRqgXo) by Mark Smith at EuroPython 2019.

# Installation
```bash
$ # install using:
$ python -m pip install md2nb
$
$ # to verify installation and show help:
$ md2nb
```

# Usage
The simplest example - in the root directory of this repo:
```bash
$ md2nb --dir . -r
Converting '.md' files within ./ and all subdirectories:
	./README.md
	./test/example.md
	./test/example-gB18030.md
```

In short, use `md2nb PATH_TO_FILE1 PATH_TO_FILE2`, or `md2nb --dir PATH_TO_DIRECTORY1 PATH_TO_DIRECTORY2`. There are two recommended ways of using `md2nb`:
1. `md2nb` converts all files with `--ext` specified extensions in the `--dir` specified directories into `.ipynb` files with a single Markdown block. For example:
    ```bash
    # to convert all Markdown and text files in the current directory and all of its subdirectories
    $ md2nb --dir . -r --ext .md .txt
    ```
2. `md2nb` converts all files identified by their file paths. For example:
    ```bash
    # to convert all Markdown files in the current directory and all of its subdirectories
    $ md2nb *.md -r
    ```
3. In fact, these two ways can be combined. For example:
    ```bash
    # to convert README, LICENSE, all .md and .txt files in . and ./doc/
    $ md2nb README LICENSE --dir . doc --ext .md .txt
    ```
