# HyP3 documentation

HyP3 documentation is build using [MkDocs](https://www.mkdocs.org/) and the
[Material theme](https://squidfunk.github.io/mkdocs-material/). 

## How to

From the repository root, you can setup a conda environment with all the 
necessary dependencies

```
conda env create -f conda-env.yml
```

then, to build and view the documentation locally

```
mkdocs serve
```

which will allow you to view the documentation at http://127.0.0.1:8000/. This
make target will automatically watch for new/changed files in this directory and
rebuild the website so you can see your changes live (just refresh the webpage!).

*Note: Because this captures your terminal (`crtl+c` to exit), it's recommended you
run this in its own terminal.*
