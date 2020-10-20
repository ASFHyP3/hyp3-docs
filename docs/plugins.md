# Plugins
Plugins are the science backbone of HyP3; they do all of the data processing and product generation.
Plugins can be added to HyP3 to generate new science products, or support different
tools/software/algorithms/options/etc that are not currently supported by HyP3.

## How plugins work
At their most basic level, HyP3 plugins are Docker containers with an interface (entrypoint) HyP3 understands.
Plugins handle the entire processing workflow for a single product, including:

* Marshaling the required input data
* performing any needed transformations and computations on the data
* creating the final product
* uploading the product to an AWS S3 bucket for distribution

By encapsulating the entire workflow for generating a single product, HyP3 can arbitrarily scale to meet user need.

## Developing a plugin
To create a new HyP3 plugin, we recommend starting from a Minimal Working Example (MWE) of generating
the product you're plugin will generate. Importantly, the MWE should be entirely self contained, and
include all the necessary data to generate the product.

Once a MWE is developed, it's important to define your plugin's interface  -- this is where HyP3 connects
the product generation and users. When designing the interface, you may find it helpful to ask yourself:

* what options do I want to provide to users?
* what's the *minimal* set information I need to gather from users?
    * is this information easily input by users?
    * is this information serializable? For example, can the information be written in a JSON file?
    * could I define this information more simply?

Once a MWE is developed and an interface is defined, you can use our 
[HyP3 plugin cookiecuter](https://github.com/ASFHyP3/hyp3-cookiecutter)
to help you build a plugin that conforms to the plugin requirements.

### Plugin requirements
In order to be supported by HyP3, a plugin must meet a few requirements:

* the plugin must be a Docker image that is hosted in a repository where HyP3 will be able to pull it
* the plugin's entrypoint must minimally accept the following arguments
    * `--bucket BUCKET-NAME` where `BUCKET-NAME` is the name of an AWS S3 bucket that output products will be uploaded to
    * `--bucket-prefix BUCKET-PREFIX` where `BUCKET-PREFIX` is a string appended to the key of any file uploaded to AWS S3
    (this is effectively a subfolder in AWS S3)
    * `--username USER` where `USER` is the username used to authenticate to EarthData Login
    * `--password PASSWORD` where `PASSWORD` is the password used to authenticate to EarthData Login
* any necessary user input should be able to be provided through entrypoint arguments
* when uploading files to the S3 Bucket
    * products files must be tagged with `filetype: product`
    * if you wish to upload thumbnails or browse images, they must be tagged `filetype: thumbnail` or `filetype: browse`
      respectively
    
    *Note: the `aws` subpackage of `hyp3lib` provides helper functions for tagging and uploading files*

### Add the plugin to HyP3
Once the plugin itself is created, it can be added to the HyP3 system by... TBD.
