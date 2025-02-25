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

### Creating ARIA S1 GUNWs using HyP3
If ARIA S1 GUNWs are not available for your area or reference/secondary date combination of interest, you can create new ARIA S1 GUNWs using the HyP3 on-demand system.

**Note: The lists of reference and secondary granules and the ARIA frame ID must be carefully selected to result in a valid ARIA product. See the [framing](#aria-frame-ids "Jump to framing section of this document") section for more details.**

#### On-Demand via the HyP3 SDK
ARIA S1 GUNW products can be generated using the Python-based HyP3 SDK via the submit_aria_s1_gunw_job function. These function takes four arguments:
- List of reference granules
- List of secondary granules
- ARIA frame ID
- (Optional) HyP3 job name

#### On-Demand via Vertex
On-demand ARIA S1 GUNW generation via Vertex is not currently available, but we plan to make this available in the future. We expect to have this available in the second half of 2025.


#### ARIA Frame IDs
Sentinel-1 SLC products are not created in a way that ensures that granules for the same relative orbit and location but different dates always fully overlap. This results in a frame “jitter” that can make it difficult to create long time series of Sentinel-1 InSAR products.

To address this issue, the ARIA team defined a standard set geographic footprints (i.e., frames) that set the geographic extent for each ARIA-S1-GUNW products. This is possible because while the Sentinel-1 SLC products exhibit jitter along the orbit, the smaller burst SLCs that each Sentinel-1 SLC product is composed of do a have fixed footprint (e.g., the bursts contained within a given Sentinel-1 SLC product changes based on the acquisition). Thus ARIA-S1-GUNW frames are defined via the specific bursts that each ARIA-S1-GUNW product contains. **ARIA-S1-GUNWs containing the same bursts, and thus sharing same geographic footprint, are said to have the same ARIA Frame ID.**

To ensure that ARIA-S1-GUNW products are always created using the standard footprints, the ARIA Frame ID along with the reference and secondary granules that intersect this footprint for a given date need to be provided in order to create a new ARIA-S1-GUNW product.

It can be tricky to find the appropriate granules for a given ARIA Frame ID, and in the future we plan to create utilities to simplify this process. For the meantime, a geojson detailing the ascending ARIA Frame IDs can be downloaded [here](https://d3g9emy65n853h.cloudfront.net/ARIA_S1_GUNW/ascending.geojson){target=_blank} and a geojson detailing the descending ARIA Frame IDs can be downloaded [here](https://d3g9emy65n853h.cloudfront.net/ARIA_S1_GUNW/descending.geojson){target=_blank}.

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