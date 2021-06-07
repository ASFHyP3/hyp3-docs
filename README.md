# HyP3 documentation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4646138.svg)](https://doi.org/10.5281/zenodo.4646138)

HyP3 documentation is built using [MkDocs](https://www.mkdocs.org/) and the
[ASF Theme](https://github.com/ASFHyP3/mkdocs-asf-theme).

## How to

### Setting up a development environment

In order to automatically document some of our APIs, we use a `conda` environment
with our APIs installed. You can get Miniconda (recommended) here:

<https://docs.conda.io/en/latest/miniconda.html>

Once conda is installed, from the repository root, you can create and activate a 
conda environment with all the necessary dependencies

```
conda env create -f environment.yml
conda activate hyp3-docs
```

Later, you can update the environment's dependencies with

```
conda env update -f environment.yml
```

### Build and view the documentation site

With the `hyp3-docs` conda environment activated, run

```
mkdocs serve
```

to generate the documentation. This will allow you to view it at <http://127.0.0.1:8000/>.
MkDocs will automatically watch for new/changed files in this directory and
rebuild the website so you can see your changes live (just refresh the webpage!).

*Note: `mkdocs serve` captures your terminal; use `crtl+c` to exit. It is recommended you
use a second/dedicated terminal so you can keep this command running.*

### Deploy

This documentation site is deployed as a Github Organization website with a CNAME
so that it's viewable at <https://hyp3-docs.asf.alaska.edu/>. The website is served
out of the special <https://github.com/ASFHyP3/ASFHyP3.github.io> repository. Deployment
is handled automatically with the `.github/workflows/deploy_to_github_io.yml` Github
Action for any merge to `main`.

There is also a test site deployed to <https://hyp3-docs.asf.alaska.edu/hyp3-docs>, which
tracks the `develop` branch of this repo and is served out of the `gh-pages` branch
of this repo.

## Markdown formatting

The way MkDocs and GitHub parse the markdown documents are slightly different. Some compatibility tips:

* Raw links should be wrapped in angle brackets: `<https://example.com>`
* MkDocs is pickier about whitespace between types (e.g., headers, paragraphs, lists) and seems to 
expect indents to be 4 spaces. So to get a representation like:

    <hr/>
    
    - A list item
    
         ##### A sub list heading
        - A sub-list item
    
    <hr/>
      
    in MkDocs, you'll want to write it like: 
        
    ### Good
    ```
    - A list item
    
        ##### A sub list heading
        - A sub-list item
    ```
    
    ### Bad
    ```
    - A list item
      ##### A sub list heading
      - A sub-list item
    ```
    
    ```
    - A list item
        ##### A sub list heading
        - A sub-list item
    ```
    
    ```
    - A list item
    
      ##### A sub list heading
      - A sub-list item
    ```
