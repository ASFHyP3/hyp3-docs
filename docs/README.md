# HyP3 documentation

HyP3 documentation is build using [sphinx](https://www.sphinx-doc.org/en/master/), 
the [MyST markdown parser](https://myst-parser.readthedocs.io/en/latest/index.html)
and the [Material theme](https://bashtage.github.io/sphinx-material/index.html). 

## How to

From this (`docs`) directory, you can setup a conda environment with all the
necessary dependencies

```
conda env create -f conda-env.yml
```

then, to build and view the documentation locally

```
make livehtml
```

which will allow you to view the documentation at http://127.0.0.1:8000/. This
make target will automatically watch for new/changed files in this directory and
rebuild the website so you can see your changes live (just refresh the webpage!).

*Note: Because this captures your terminal (`crtl+c` to exit), it's recommended you
run this in its own terminal.*
