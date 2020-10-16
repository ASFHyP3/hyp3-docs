# HyP3 documentation

HyP3 documentation is build using [MkDocs](https://www.mkdocs.org/) and the
[Material theme](https://squidfunk.github.io/mkdocs-material/). 

## How to

### setting up a development environment

From the repository root, you can setup a conda environment with all the 
necessary dependencies

```
conda env create -f conda-env.yml
```

### build and view the documentation site
```
mkdocs serve
```

which will allow you to view the documentation at http://127.0.0.1:8000/. This
make target will automatically watch for new/changed files in this directory and
rebuild the website so you can see your changes live (just refresh the webpage!).

*Note: Because this captures your terminal (`crtl+c` to exit), it's recommended you
run this in its own terminal.*

### Deploy

This documentation site is deployed as a Github Organization websites at
https://asfhyp3.github.io/, which is served out of the special
https://github.com/ASFHyP3/ASFHyP3.github.io repository. To deploy you'll need to
have cloned `ASFHyP3.github.io` *somewhere outside of this repo*. Then to deploy:

```
cd PATH/TO/ASFHyP3.github.io
mkdocs gh-deploy --config-file PATH/TO/ASFHyP3/mkdocs.yml --remote-branch main
```

## Markdown formatting

The way MkDocs and GitHub parse the markdown documents are slightly different. Some compatibility tips:

* Raw links should be wrapped in carrots: `<https://example.com>`
* MkDocs is pickier about whitespace between types (e.g., headers, paragraphs, lists) and seems to 
expect indents to be 4 spaces, so to get a representation like:

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
