import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="md2nb",  # Replace with your own username
    version="0.0.1",
    author="Qin Yu",
    author_email="qin.yu@embl.de",
    license="bsd-3-clause",
    description="Convert Markdown files to Jupyter notebooks with a single Markdown block",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qin-yu/md2nb",
    packages=setuptools.find_packages(),
    # py_modules=["md2nb"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Markup :: Markdown"
    ],
    keywords="markdown jupyter notebook md ipynb",
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'md2nb=md2nb.md2nb:md2nb_all',
        ],
    },
)
