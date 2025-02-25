{% extends "guides/insar_product_guide_template.md" %}

{% block header %}
# Sentinel-1 GUNW Product Guide

This document is a guide for users of Sentinel-1 Geocoded Unwrapped (GUNW) Interferometric Synthetic Aperture Radar (InSAR) products.  

### ARIA Sentinel-1 GUNWs
High-level GUNW interferograms are produced as a part of the [Jet Propulsion Lab (JPL)'s Advanced Rapid Imaging and Analysis (ARIA) Project](https://aria.jpl.nasa.gov/){target=_blank}. 
* Analysis ready products including a geocoded unwrapped interferogram
* ARIA-S1-GUNW is an official NASA product
* Initially developed as part of the Getting Ready for NISAR 
* Generated using an ISCE2 InSAR workflow [TopsApp](https://github.com/isce-framework/isce2-docs/blob/master/Notebooks/UNAVCO_2020/TOPS/topsApp.ipynb){target=_blank} 
  * [ISCE2](https://github.com/isce-framework/isce2){target=_blank} InSAR workflow for S1 SLCs corresponding to a repeat-pass date
* Output L2 standard displacement product in NetCDF4 format

{% endblock %}

{% block acquiring_products %}
### Acquiring products
* GUNW products are available on [Earthdata Search](https://search.earthdata.nasa.gov/search){target=_blank} and [Vertex](https://search.asf.alaska.edu/#/?dataset=SENTINEL-1%20INTERFEROGRAM%20(BETA)){target=_blank}
* If your desired GUNW does not exist, products can be acquired using HyP3

#### Archive on Earthdata Search
* GUNW products are available on [Earthdata Search](https://search.earthdata.nasa.gov/search){target=_blank} and [Vertex](https://search.asf.alaska.edu/#/?dataset=SENTINEL-1%20INTERFEROGRAM%20(BETA)){target=_blank}
* * Earthdata Search requires NASA Earthdata user login. (See ["What do I need to know about Earthdata login?"](https://urs.earthdata.nasa.gov/documentation/what_do_i_need_to_know#:~:text=Simply%2C%20go%20to%20http%3A%2F%2F,of%20data%20user%20you%20are){target=_blank}
* Search the ARIA S1 Geocoded Unwrapped Interferograms collection
  * Can be refined with search parameters for date, etc

#### Searching using Vertex
* If your desired GUNW does not exist, you can submit to HyP3

#### Submitting GUNWs using HyP3
* HyP3 accepts ARIA-S1-GUNW jobs
* required parameters are reference granules, secondary granules and a frame_id
* Interfaces to be further developed to aid in the search for appropriate frame_ids and granules on Vertex
* An example job would be ... # TODO : find an example job? 

#### Frame IDs vs Granules
* In addition to reference and secondary scenes, a frame-id must be provided
* This is what makes the ARIA-S1-GUNW product "standard"
  * Done to ensure down-stream analysis is consistent and reproducible
* Restricts the resulting product to be within this frame
* geojson with S1 Frames is available in the [DockerizedTopsApp GitHub Repository](https://github.com/ACCESS-Cloud-Based-InSAR/DockerizedTopsApp/blob/dev/isce2_topsapp/data/s1_frames_latitude_aligned.geojson.zip){target=_blank}
* Note that it can be tricky to find an appropriate frame-id for granule selection
  * Future work will be done to aid this process

{% endblock %}

{% block standard_products %}

### Output of standard product
L2 ARIA-S1-GUNW standard product is packaged as a NetCDF4 file. 

The output netCDF file will include the layers listed in Table 2 below.

| Group           | Dataset Name             | Description                                  | Units    |
|-----------------|--------------------------|----------------------------------------------|----------|
| data            | amplitude                | 2D Amplitude of IFG                          | watt     |
|                 | coherence                | 2D Coherence [0-1] from filtered IFG         | unitless |
|                 | connectedComponents      | 2D Connected component file                  | unitless |
|                 | unfilteredCoherence      | 2D Coherence [0-1] from unfiltered IFG       | unitless |
|                 | unwrappedPhase           | 2D Filtered unwrapped IFG geocoded           | rad      |
| corrections     | ionosphere               | 2D Split spectrum ionospheric delay          | rad      |
|                 | ionosphereBurstRamps     | Digital elevation model                      | rad      |
|                 | reference/solidEarthTide | 2D/3D solid earth tide for reference granule | rad      |
|                 | secondary/solidEarthTide | 2D/3D solid earth tide for secondary granule | rad      |
| imagingGeometry | azimuthAngle             | 3D azimuth angle grid                        | degree   |
|                 | incidenceAngle           | 3D Incidence angle grid                      | degree   |
|                 | lookAngle                | 3D look angle grid                           | degree   |
|                 | parallelBaseline         | 3D parallel baseline grid                    | meter    |
|                 | perpendicularBaseline    | 3D perpendicular baseline grid               | meter    |

*Table 2: Layers in standard ARIA-S1-GUNW netCDF file. *

{% endblock %}

{% block algorithm %}

### Algorithm
* Standard products are produced using [DockerizedTopsApp](https://github.com/ACCESS-Cloud-Based-InSAR/DockerizedTopsApp){target=_blank}
* Tropospheric corrections for RADAR are calculated using the [Raytracing Atmospheric Delay Estimation for RADAR (RAiDER)](https://github.com/dbekaert/RAiDER){target=_blank} package. 

#### Weather model
* built-in support for different weather models through RAiDER
* [High-resolution rapid refresh (HRRR)](https://rapidrefresh.noaa.gov/hrrr/){target=_blank} weather model generated by NOAA for continental US
* Available for continental US and Alaska
* Spatial resolution of about 3 km
* If there is no weather data available for AOI, no weather model will be applied

#### Metrics around Accuracy
* @Forrest did you have thoughts of what should go here? 

{% endblock %}