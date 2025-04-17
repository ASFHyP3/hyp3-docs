# OPERA RTC for Sentinel-1 (RTC-S1) Product Guide

This document is a guide for users of the 
[OPERA Radiometric Terrain Corrected Backscatter for Sentinel-1 (RTC-S1)](https://www.jpl.nasa.gov/go/opera/products/rtc-product/ "www.jpl.nasa.gov/go/opera/products/rtc-product" ){target=_blank} 
products. These products were developed by the 
[Observational Products for End-Users from Remote Sensing Analysis (OPERA)](https://www.jpl.nasa.gov/go/opera/ "www.jpl.nasa.gov/go/opera" ){target=_blank} 
project at NASA's Jet Propulsion Laboratory (JPL).

!!! tip "OPERA RTC-S1 Products Now Available On Demand"

    If OPERA RTC-S1 products are not available for your full time range or area of interest, you can now request that
    they be processed On Demand! 

The OPERA project has generated the RTC-S1 products for all Sentinel-1 acquisitions over landmasses (except Antarctica) 
since January 1, 2022. OPERA continues to process new Sentinel-1 SLCs to RTC-S1 as they become available in ASF's 
archive. These products are all available for download from ASF, using ASF's 
[Vertex Data Search](https://search.asf.alaska.edu/#/?dataset=OPERA-S1&productTypes=RTC "search.asf.alaska.edu" ){target=_blank} 
interface, the 
[asf_search python package](https://docs.asf.alaska.edu/asf_search/basics/ "docs.asf.alaska.edu" ){target=_blank}, 
or through 
[Earthdata Search](https://search.earthdata.nasa.gov/search/granules?p=C2777436413-ASF "search.earthdata.nasa.gov" ){target=_blank}. 

You can also order OPERA RTC-S1 products from ASF on demand. This is particularly useful if you need a time 
series of RTC-S1 products that extends beyond the start of the archive. On-Demand processing is available for any 
Sentinel-1 burst with the same burst ID (footprint) as an existing OPERA RTC-S1 product. 

On-Demand RTC-S1 products are generated using the same code that is used by the OPERA project, but are processed 
using ASF's 
[HyP3](https://hyp3-docs.asf.alaska.edu/){target=_blank} 
cloud-native processing platform instead of JPL's 
[OPERA SDS](https://software.nasa.gov/software/NPO-52101-1){target=_blank} 
processing management software. The products can be used interchangeably in a time series analysis.

A Digital Elevation Model (DEM) is required for radiometric terrain correction. The 
[GLO-30 Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM "Copernicus DEM" ){target=_blank}
is used to process the OPERA RTC-S1 On Demand products. 

For more information on options for accessing archived OPERA RTC-S1 products, refer to ASF's 
[OPERA Sentinel-1 RTC Tutorial](https://storymaps.arcgis.com/stories/dc2807b444924fc3a76c117a2c909f8b "OPERA Sentinel-1 RTC StoryMap Tutorial" ){target=_blank}. 
For more information on the technical specifications of the OEPRA RTC-S1 products, refer to JPL's 
[RTC Product Documentation](https://www.jpl.nasa.gov/go/opera/products/rtc-product/ "OPERA RTC Product" ){target=_blank}.

## RTC Products from ASF

In addition to OPERA RTC-S1 products, which use JPL's open-source 
[ISCE3 software](https://github.com/isce-framework/isce3 "github.com/isce-framework/isce3" ){target=_blank} 
to perform radiometric terrain correction, ASF also offers 
[On-Demand RTC products](rtc_product_guide.md "Sentinel-1 RTC Product Guide" ){target=_blank} 
generated using commercial [GAMMA](https://gamma-rs.ch/gamma-software "gamma-rs.ch/gamma-software" ){target=_blank} 
SAR processing software. 

These products are both high-quality Sentinel-1 RTC options, and you can use either with confidence for any given 
RTC-based analysis workflow. Because the products do use different algorithms for the RTC processing, however, 
a time-series analysis will be more consistent if you don't mix and match products generated using GAMMA and ISCE3. 

There are some key characteristics that differ between the two products, which may help you decide which would be 
most appropriate for your particular application. 

### Spatial Extent


### Processing Options


### RGB Decomposition





## Ordering On-Demand OPERA RTC-S1 Products




## Product Packaging


