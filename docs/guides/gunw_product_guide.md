{% extends "guides/insar_product_guide_template.md" %}

{% block header %}
# Sentinel-1 GUNW Product Guide

This document is a guide for users of Sentinel-1 Geocoded Unwrapped (GUNW) Interferometric Synthetic Aperture Radar (InSAR) products.  

### ARIA Sentinel-1 GUNWs
The ARIA Sentinel-1 Geocoded Unwrapped Phase (ARIA-S1-GUNW) product is a standardized InSAR dataset that enables rapid analysis of surface deformation using Sentinel-1 SAR data. Produced by [NASA’s ARIA](https://aria.jpl.nasa.gov/){target=_blank} project and hosted at the Alaska Satellite Facility (ASF) DAAC, it provides 90-meter resolution, CF-compliant NetCDF files containing unwrapped interferometric phase, imaging geometry, tropospheric delay estimates, and metadata. With over 1.1 million (and growing!) freely available products covering major fault systems, volcanic regions, and coastal zones, ARIA-S1-GUNW facilitates scientific research and disaster response by simplifying access to centimeter-scale ground displacement measurements. Generated through an open-source, cloud-based [ISCE2 TopsApp processing pipeline](https://github.com/isce-framework/isce2-docs/blob/master/Notebooks/UNAVCO_2020/TOPS/topsApp.ipynb){target=_blank}, these products support applications such as earthquake impact assessment, volcanic monitoring, and long-term land motion studies, with ongoing improvements enhancing their accuracy and usability.

{% endblock %}

{% block accessing_products %}
### Accessing Products

You can download ARIA-S1-GUNW products from the Alaska Satellite Facility’s (ASF) [Vertex](https://search.asf.alaska.edu/#/?dataset=SENTINEL-1%20INTERFEROGRAM%20(BETA)){target=_blank} search portal by following these steps: 
1. **Access Vertex** – Go to the ASF Vertex website: https://search.asf.alaska.edu.
2. **Search for ARIA-S1-GUNW Products** – In the dataset selector, click on “ARIA S1 GUNW” to filter for these specific products. You can refine results by specifying a geographic region, date range, or other criteria using the search filters in the “filters” panel.
![Vertex ARIA S1 GUNW Dataset Selection](../images/vertex-GUNW-dataset-selection.png)
3. **Preview and Select Products** – Click on individual results to view metadata, including coverage area and acquisition details.
4. **Download Data** – To download, first add ARIA S1 GUNW products to your download queue using the shopping cart icon next to each product, then download your select products using the “download” panel.

You can also use the Vertex SBAS tool to download networks of interferograms for a specific location. See [this guide](https://docs.asf.alaska.edu/vertex/sbas/){target=_blank} for more information.

**NOTE: ARIA S1 GUNW products are not produced globally! If you cannot find ARIA S1 GUNW for your area of interest, see the On-Demand section below.**

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