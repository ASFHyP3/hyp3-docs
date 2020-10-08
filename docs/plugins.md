# Plugins
Plugins are an important part of HyP3, they are the component that actually does all of the computation when processing SAR data. Different plugins can be added to hyp3 to support different SAR processing tools, or options not available in current products.

## How Plugins Work
Plugins are implemented as Docker containers, this allows them to encapsulate complicated science code and abstract the interface to one entry point. 

In order to be supported by HyP3 the plugin must meet a few requirements:
* Plugin entrypoint must accept the following arguments
  * `--bucket-prefix s3-prefix` where `s3-prefix` is appended to the key of any file uploaded to aws S3
  * `--bucket bucket-name` where `bucket-name` is an AWS S3 bucket that output products will be uploaded to.
  * `--username user` where user is the username used to authenticate to EarthData Login.
  * `--password user` where password is the password used to authenticate to EarthData Login.
  * Other parameters should be included to take any required input from the user.
* Output products must be tagged with `filetype: product`, if you wish to upload thumbnails or browse images, they must be tagged `filetype: thumbnail` or `filetype: browse` respectively.
* Plugin must be a Docker container that is hosted in a repository where ASF HyP3 will be able to pull it from AWS.

Once the plugin itself is created, it can be added to the hyp3 system. see [adding a plugin](FOO)
