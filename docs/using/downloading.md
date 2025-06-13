# Downloading HyP3 Products

There are a number of interfaces available for downloading products generated On Demand using the HyP3 platform. 

- [On Demand Search](#on-demand-search-in-vertex) interface in Vertex
- Programmatically using the HyP3 API or HyP3 Python SDK

## On Demand Search in Vertex

The [On Demand Search](https://search.asf.alaska.edu/#/?maxResults=1000&searchType=On%20Demand "Vertex On Demand Search" ){target=_blank} 
in Vertex allows you to view the status of any job you have submitted for processing and download any product 
that has been successfully processed. You will need to sign in with 
[Earthdata Login credentials](https://urs.earthdata.nasa.gov/ "urs.earthdata.nasa.gov" ){target=_blank} 
before results will display.

Refer to the 
[On Demand Search section of the Vertex User Manual](https://docs.asf.alaska.edu/vertex/manual/#on-demand-products-search-options "docs.asf.alaska.edu" ){target=_blank} 
for more information. 

### Downloading Individual Products

Click on an item in the search results to view download options. You can add the product to the Download Queue using 
the **cart icon** in either the Search Result (left) or File (right) pane, or launch a direct download in your 
browser window by clicking the **cloud download icon** in the file pane. 

![Downloading Individual Products](../images/download-vertex-single.png "Download Single On Demand Product")

To view the download queue, click the **Downloads** icon in the top band of the Vertex web interface. 
The Download Queue interface provides options for direct download of individual items along with bulk download options.

### Downloading Multiple Products

You can add products to the Download Queue one by one using the cart icon, or you can search your On Demand 
products for a specific set of products and add them all to the Download Queue using the **Queue** button at the 
top of the results list. 

![Downloading Multiple Products](../images/download-vertex-multiple.png "Download Multiple On Demand Products")

There are a number of options available for filtering your On Demand products, with the most useful being the 
**Project Name** field. You can assign a project name when submitting jobs for processing to easily group items 
together that are used for the same project. 

Once you've added products to the Download Queue, either by using the individual cart icons or the bulk Queue 
button, click the **Downloads** icon in the top band of the Vertex web interface. When you open the Download Queue, 
you have the option to launch direct downloads of individual items in the list, or you can choose to remove 
individual items from the queue. 

To download all of the products listed in the Download Queue, click the **Data Download** button at the bottom of 
the queue window and choose from the available options. 

The most robust approach for downloading very long lists of products is the 
**Download Python Script** option. This downloads a python script that you can launch on your computer. 

- You will be prompted for your Earthdata Login credentials, then the script will work through the list of 
  download URLs, downloading them one by one until all of the items have been downloaded. 
- If the script is interrupted during the download, you can simply re-run the same script; it will recognize 
  any products that have already been successfully downloaded and continue with the remaining items. 
- To use this option, you must have a Python installation available on your computer. 

Chrome users may find the **Download All** option useful. This option takes advantage of the multi-threading  
capability in Chrome to download several items at a time.

You can also click the option to **Copy URLs**, which you can then paste into your own download script, 
if you'd prefer. 

## Using HyP3 API or HyP3 Python SDK

<!-- [TODO: Populate this section] -->




## Product Packaging and Extraction

On Demand products from ASF are delivered as zip files. The files contained in the zip archive vary by product type, 
but the zip archive always includes an internal directory containing all the individual files. The directory names 
can be quite long, and some users (particularly those using a Windows operating system) will need to make 
accommodations in order to successfully extract the contents.

### Extracting Product Packages

When extracting the contents of a HyP3-generated zip file, you may need to specify a destination directory to prevent 
the extraction of the internal directory to a directory named with the full zip file name. For many of the products, 
this combination of directories would result in paths that are longer than can be used with Windows operating systems. 

### Accessing Individual Products

On Demand products are delivered as zip files for ease of downloading. Downloading the full zip file ensures that 
you have all of the data products as well as auxiliary files and relevant metadata. 

Some users may not require all of the files included in the product zip archive. The contents of the zip files 
can all be accessed directly. Simply replace the .zip at the end of the download URL with the tag for the 
specific file you want to download. 

For example, for the following download URL for an RTC On Demand product: 
`https://d3gm2hf49xd6jj.cloudfront.net/76b1a849-c826-428a-966c-55f8bb88f814/S1A_IW_20250502T135654_DVP_RTC30_G_gpuned_70DD.zip`

simply replace the .zip with the product extension, such as the following for the RTC GeoTIFF in VV polarization: 
`https://d3gm2hf49xd6jj.cloudfront.net/76b1a849-c826-428a-966c-55f8bb88f814/S1A_IW_20250502T135654_DVP_RTC30_G_gpuned_70DD_VV.tif`

You can then paste that URL into a browser window, or use it in a download script, to access only the designated 
product rather than the full zip archive. 

Note that the zip archive contains valuable metadata products, including a readme file that provides information 
about the workflow used to generate the product and the files included in the product package. New users should 
download the full archive to ensure they have access to this information and can determine what individual products 
they would require for their application. 
