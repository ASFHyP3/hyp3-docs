# Sentinel-1 RTC Product Guide

This document is a guide for users of radiometrically terrain-corrected Sentinel-1 products processed by the Alaska Satellite Facility.

## Data Processing

### Digital Elevation Models

The quality of the terrain correction results is directly related to the quality of the digital elevation models (DEMs) used in the process of geometrically and radiometrically correcting the SAR imagery. Table 1 summarizes the various DEM sources and the way they are used in the radiometric terrain correction (RTC).

| Resolution | DEM | Datum | Area | Posting | Sampling |
|------------|-------|--------|------|---------|----------|
| High | NED13 | NAVD88 | CONUS, Hawaii, parts of Alaska | 1/3 arc seconds | Resampled to RTC spacing, reprojected to WGS84 UTM |
| Medium | SRTMGL1 | EGM96 | 60 N to 57 S latitude | 1 arc second | Resampled to RTC spacing, reprojected to WGS84 UTM |
| Medium | SRTM US1 | EGM96 | CONUS, Hawaii, parts of Alaska | 1 arc second | Resampled to RTC spacing, reprojected to WGS84 UTM |
| Medium | NED1 | NAVD88 | CONUS, Hawaii, parts of Alaska, Canada, Mexico | 1 arc second | Resampled to RTC spacing, reprojected to WGS84 UTM |
| Medium | NED2 | NAVD88 | Alaska | 2 arc seconds | Resampled to RTC spacing, reprojected to WGS84 UTM |

*Table 1: DEMs used and their priority in RTC processing*

Figure 1 shows the coverage of the various DEM sources. The continental U.S. (CONUS), Hawaii, and parts of Alaska are covered by the National Elevation Dataset (NED) at ⅓ arc seconds (about 10 m resolution). The rest of Alaska above 60 degrees northern latitude is only available at about 60 m resolution with 2 arc seconds NED data. The best resolution for Canada and Mexico is provided by the 1 arc second NED at about 30 m. For the remaining globe, Shuttle Radar Topography Mission (SRTM) GL1 data at 30 m resolution is used. Greenland and Antarctica are mostly covered by ice and glaciers and not suitable for terrain correction. For areas in Eurasia above 60 degrees northern latitude, no suitable DEMs are available.

![alt_text](images/image1.png "image_tooltip")

*Figure 1: Coverage of the various DEM sources used for terrain correction*

The DEMs were pre-processed by ASF to a consistent raster format (GeoTIFF) from the original source formats: height (\*.hgt), ESRI ArcGrid (\*.adf), etc. Many of the NASA-provided DEMs were provided as orthometric heights with EGM96 vertical datum. These were converted by ASF to ellipsoid heights using the ASF [MapReady](https://asf.alaska.edu/how-to/data-tools/data-tools/#mapready) tool named *geoid_adjust*. The pixel reference varied from the center (pixel as point) to a corner (pixel as area). The GAMMA software, used to generate the terrain corrected products, uses pixel as area and adjusts DEM coordinates as needed. Where more than one DEM is available, the best-resolution DEM is used for processing. DEM coverage of at least 20% from a single DEM source is required for processing to proceed.

## Terrain Correction Workflow

### Pre-processing

The first step of pre-processing is the selection of the best DEM for the terrain correction. The DEM tiles are assembled to ensure sufficient coverage for the terrain correction of the Sentinel-1 granule. The application of the calibration parameters and multi-looking are the only pre-processing steps applied to the SAR image.

### Terrain Correction

The terrain correction is performed in slant range geometry. The actual mapping of the initial image into projected space is only applied once to mitigate the propagation of any resampling errors. All intermediate steps only update the look-up table used for the mapping.

By default, images are not coregistered to the DEM. While RTC results can be improved by matching imagery to a high-quality DEM, many of the available DEMs will cause a shift in the geolocation of the imagery when DEM matching is applied. This can introduce spatial inconsistencies to the dataset, especially when viewing a time-series of RTC images. For consistency, we use the geolocation from the Sentinel-1 state vectors rather than matching the geolocation based on DEM features.

When custom-ordering imagery, however, the DEM Matching option is available for selection. In this case, the first step is the co-registration of the SAR image with a simulated SAR image derived from the DEM. An initial offset is first attempted as a single match; if it fails, a larger number of image chips are used to determine an average offset in azimuth and range direction. This initial offset is then refined using strict matching criteria. Matching may fail for three different reasons: (1) no match can be found, (2) the magnitude of the residual offset errors is greater than 2 pixels, or (3) the maximum calculated offset is greater than 50m. In any of these cases, the _dead reckoning _approach is taken when matching fails. This approach solely relies on the geolocations calculated from state vectors (the same approach used when DEM matching is not selected as an option) - no geolocation refinement is applied.

A normalization area image is generated. The terrain correction results in a radiometrically calibrated multi-looked image with gamma-nought (γ<sub>0</sub>) power scale values. The ratio between the pixel area of the uncorrected and the corrected images is determined and stored in an image. In order to create the RTC product, the SAR image is multiplied by the ratio image. In a final step the RTC product is geocoded into map-projected space.

### Post-Processing

After the terrain correction is completed, the RTC products are exported to GeoTIFF format. Side products including the DEM, layover shadow map, and incidence angle file are converted into GeoTIFF format. In addition, a README text file, browse images, item-specific ArcGIS-compatible XML metadata files, a log file, a shapefile, and an XML metadata file in ISO 19115-2 format are generated for the product.

## Product Packaging

### Naming Convention

The naming convention for the RTC products follows this pattern for its base names:

S1x_yy_aaaaaaaaTbbbbbb_ppo_RTCzz_G_defklm_ssss

Example: S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A

| Element | Definition | Example |
|---|---|---|
| x | Mission: A or B | A |
| yy | Beam Mode | IW |
| aaaaaaaa | Start Year-Month-Day | 20180128 |
| bbbbbb | Start Hour-Minute-Second | 161201 |
| pp | Polarization | DV |
| o | Orbit Type: Precise (P), Restituted (R), or Original Predicted (O) | P |
| zz | Terrain Correction Resolution (m) | 30 |
| d | Gamma-0 (g) or Sigma-0 (s) Output | g |
| e | Power (p) or Amplitude (a) Output | p |
| f | Unmasked (u) or Water Masked (w) | u |
| k | Not Filtered (n) or Filtered (f) | n |
| l | Entire Area (e) or Clipped Area (c) | e |
| m | Dead Reckoning (d) or DEM Matching (m) | d |
| ssss | Product ID | FD6A |

*Table 2: Naming convention for RTC products*

### Default Settings

The default settings for RTC products are as follows:

Radiometry: Gamma-0 (g)

Scale: Power (p)

Water Mask: No water mask applied (u)

Speckle Filter: Not filtered (n)

Clipping: Entire extent of input granule (e)

DEM Matching: No matching; dead reckoning is used (d)

### Image Files

All files are stored in a folder named using the above convention, and the base name for each file matches the folder name. Multiple types of image files are present in this folder.

| Extension | Description | Example |
|---|---|---|
| _VV.tif, _VH.tif, _HH.tif, _HV.tif | Terrain corrected product stored in separate files for each available polarization in GeoTIFF format | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A_VV.tif |
| .png | Greyscale browse image | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A.png |
| _rgb.png | Color browse image | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A_rgb.png |
| .kmz | Zipped Google Earth image | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A.kmz |
| _rgb.kmz | Zipped Google Earth color image | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A_rgb.kmz |
| _dem.tif | DEM used for terrain correction in GeoTIFF format | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A_dem.tif |
| _inc_map.tif | incidence angle file in GeoTIFF format | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A_inc_map.tif |
| _ls_map.tif | layover/shadow mask in GeoTIFF format | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A_ls_map.tif |

*Table 3: Image files in product package*

Floating point GeoTIFF files are used for the main products as well as the DEM and incidence angle map. An integer GeoTIFF file is used for the layover/shadow mask. PNG format is used for both the color and the greyscale browse images, which are each 2048 pixels wide. Finally, KMZ files suitable for viewing in Google Earth are included. Note that colorized browse and KMZ images can only be created for dual-polarization (SDV and SDH) granules, not for single-polarization (SSV or SSH).

### Metadata Files

Along with each of the image files, there will be one or more metadata files.

| Extension | Description | Example |
|---|---|---|
| .README.md.txt | README file | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A.README.md.txt |
| .log | Log file of the processing steps | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A.log |
| .tif.xml | ArcGIS compliant XML metadata | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A_VV.tif.xml |
| .png.xml | ArcGIS compliant XML metadata | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A.png.xml |
| _rgb.png.xml | ArcGIS compliant XML metadata | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A_rgb.png.xml |
| .png.aux.xml | Geolocation metadata for greyscale PNG browse image | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A.png.aux.xml |
| _rgb.png.aux.xml | Geolocation metadata for color PNG browse image | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A_rgb.png.aux.xml |

*Table 4: Metadata files and their extensions*

#### README File

The text file with extension .README.md.txt explains the files included in the folder, and is customized to reflect that particular product. Users unfamiliar with RTC products should start by reading this README file, which will give some background on each of the files included in the product folder.

#### ArcGIS-Compatible XML Files

There is an ArcGIS-compatible xml file for each raster in the product folder. When ArcGIS Desktop users view any of the rasters in ArcCatalog or the Catalog window in ArcMap, they can open the Item Description to view the contents of the associated xml file. ArcGIS Pro users can access the information from the Metadata tab. These files will not appear as separate items in ArcCatalog, though if you use Windows Explorer to look at the contents of the folder you will see them listed individually. Because each one is named identically to the product it describes (with the addition of the .xml extension), ArcGIS recognizes the appropriate file as the raster’s associated metadata, and integrates the metadata accordingly.

ArcGIS users should take care not to change these xml files outside of the ArcGIS environment; changing the filename or content directly may render the files unreadable by ArcGIS.

Those not using ArcGIS will still find the contents of these xml files useful, but will have to contend with the xml tagging when viewing the files as text or in a browser.

#### Auxiliary Geolocation Files

Geolocation XML files (aux files) are included for each of the PNG browse images to allow for proper display in GIS platforms.

#### Log File

A log file detailing the processing parameters and outputs is also included for reference.

### Shapefile

A shapefile indicating the extent of the RTC data coverage is included in the package.

| Extension | Description | Example |
|---|---|---|
| _shape.dbf _shape.prj _shape.shp _shape.shx | Shapefile (.shp) and supporting files | S1A_IW_20180128T161201_DVP_RTC30_G_gpuned_FD6A_shape.shp |

## SAR Scales

### Power Scale

Note that the default output of Sentinel-1 RTC products from HyP3 is in power scale. The values in this scale are generally very close to zero, so the dynamic range of the RTC image can be easily skewed by a few bright scatterers in the image. Power scale is appropriate for statistical analysis of the RTC dataset, but may not always be the best option for data visualization.

When viewing an RTC image in power scale in a GIS environment, it may appear mostly or all black, and you may need to adjust the stretch to see features in the image. Often applying a stretch of 2 standard deviations, or setting the Min-Max stretch values to 0 and 0.3, will greatly improve the appearance of the image. You can adjust the stretch as desired to display your image to full advantage. Be aware that this does not change the actual pixel values.

In some cases, it may be desirable to convert the actual pixel values to a different scale. Two other scales commonly used for SAR data are amplitude and dB.

### Amplitude Scale

Amplitude scale is the square root of the power scale values. This brightens the darker pixels and darkens the brighter pixels, narrowing the dynamic range of the image. In many cases, amplitude scale presents a pleasing grayscale display of RTC images. Amplitude scale works well for calculating log difference ratios (see [Quantifying Change over Time](#Quantifying Change over Time)).

### dB Scale

The dB scale is calculated by multiplying 10 times the Log10 of the power scale values. This scale brightens the pixels, allowing for better differentiation among very dark pixels. When identifying water on the landscape, this is often a good scale to use; the water pixels generally remain very dark, while the terrestrial pixels are even brighter (see [Identifying Surface Water](#identifying-surface-water)).

This scale is not always the best choice for general visualization of RTC products, as it can give a washed-out appearance, and because it is in a log scale, it is not appropriate for all types of statistical analyses.

## RTC Use Examples

The RTC products are presented as Cloud-Optimized GeoTIFFs (COGs), a user-friendly format that is GIS compatible. The products do not include pre-generated overviews, so users may need to generate pyramids to display the images efficiently in a GIS environment.

The side-looking geometry of SAR imagery leads to geometric and radiometric distortions. RTC adjusts images so that the values relate to actual topographic features, alleviating shadows, foreshortening, and layover effects inherent to SAR images. These corrected images can then be used as “just another layer” within a GIS, and can be combined with other datasets in a number of ways.

The two satellites that comprise the Sentinel-1 mission each have a 12-day repeat cycle, so most areas of the earth will have imagery at least every 6 days, but many areas have coverage even more frequently, making this SAR dataset a very useful tool for monitoring rapid or sudden landscape changes. In addition, SAR is not impacted by either cloud cover or lack of light, so RTC imagery can be collected at any time, and in areas or situations where cloud cover often causes problems for other imagery types.

The following sections present examples of how one might use RTC datasets to identify areas of change and integrate RTC datasets into other datasets for enhanced results. We also present a bibliography of some of the scientific literature making use of Sentinel-1 RTC datasets.

### Change Detection Using RTC Data

There are a number of ways that SAR data sets can be used to identify areas of change. Here are two examples of what you can do in a GIS environment.

#### Seasonal Change

Stacking RTC images into a multiband image (Figure 2) allows the user to display different times of year at the same time, using the color bands to highlight areas that differ in radar backscatter values from one month to the next.

To generate this type of image, choose three images that capture different seasons or months of interest. These can either be individual RTC images from different times of the year, or rasters displaying the monthly median calculated from multiple RTC images collected in the same month.

Combine the three images into a multiband raster and assign each to a different color band. The resulting RGB image highlights areas where there are distinctive differences among the three source image values.

<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>> gd2md-html alert: inline image link here (to images/image2.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image2.jpg "image_tooltip")

*Figure 2: Monthly median VH gamma-0 power values for May, July and September, displayed as a multiband RGB (May, July, Sept) image.*

#### Quantifying Change over Time

A simple and informative approach to change detection is the calculation of the log difference between two RTC datasets from different dates. By calculating Log10(date2/date1) and applying a classified symbology, it is easy to identify areas where change occurred, as well as the direction of the change. Negative values indicate a decrease in radar backscatter over time, while positive values indicate an increase in backscatter.

In the example below (Figure 3), RTC images from before and after heavy rains caused a dam breach. The area where the reservoir was located displays a significant increase in backscatter (symbolized in red), where land once covered by standing water (which generally has very low backscatter) is now exposed and saturated with moisture (which generally returns very high backscatter values). In other surrounding areas, flooding caused decreases in radar backscatter (symbolized by blue) as agricultural fields were inundated with standing water. Areas with little change in backscatter are displayed in yellow.

<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>> gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image3.png "image_tooltip")

*Figure 3: Log Difference Raster with Classified Symbology*

### Identifying Surface Water

Calm surface water has a very low radar cross section. Most of the signal is reflected off the smooth surface, due to the high dielectric constant of freshwater, so little to none of the signal is returned as backscatter. Because of this, it is often easy to delineate surface water using a simple threshold value, where all pixels below the threshold are assumed to be water.

You can easily visualize the water extent using various thresholds by applying a classified symbology with two classes. It is often best to use dB scale datasets for identifying surface water. In many cases, there will be a bimodal distribution of values in an RTC image containing surface water, with the first peak comprised mostly of water values, and the second peak containing all the remaining values. A good first step is to select a break point between those two peaks, then adjust the value as needed to generate a good water mask (Figure 4).

<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>> gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image4.png "image_tooltip")

*Figure 4: Setting the break point to fall between the two peaks of the histogram*

Once you have determined the appropriate threshold (Figure 5), you can reclassify the RTC image to include only those pixels that fall below the threshold value, providing a water mask that can be used for analysis or to overlay with other imagery to show the water extent.

*Figure 5: Water Mask*

### Combination of RTC Image with other Remote Sensing Data

One of the main advantages of using RTC imagery with its all weather and day/night capabilities is the combination with other remote sensing data such as optical data. In the example below, the backscatter information of the Sentinel-1 SAR image (Figure 5) is used to enhance the spectral information of the optical Landsat 8 image (Figure 6) in the urban area of Pavia, Italy. Figure 7 shows the image fusion result of an IHS transformation. In this transformation the color channels red, green and blue (RGB) are first converted into a different color representation: intensity, hue and saturation (IHS). In the second step the optical intensity is replaced by the SAR image, before IHS is transformed back to RGB.


<table>
 <tr>
 <td>

<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>> gd2md-html alert: inline image link here (to images/image5.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/image5.jpg" width="" alt="alt_text" title="image_tooltip">

 </td>
 <td>

<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>> gd2md-html alert: inline image link here (to images/image6.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/image6.jpg" width="" alt="alt_text" title="image_tooltip">

 </td>
 </tr>
 <tr>
 <td>
<strong>Figure 5: Sentinel-1 RTC image</strong>
 </td>
 <td>
<strong>Figure 6: False color composite (bands 5, 4, 3) of a Landsat 8 image</strong>
 </td>
 </tr>
 <tr>
 <td>

<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>> gd2md-html alert: inline image link here (to images/image7.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/image7.jpg" width="" alt="alt_text" title="image_tooltip">

 </td>
 <td>The color values for the two rivers in the SAR image are far more similar to each other than in the optical image. The vegetated areas (highlighted in red) show up more uniformly in the data fusion result than in the optical false color composite image. Image fusion uses the complementary nature of the different sources to generate an enhanced product.
 </td>
 </tr>
 <tr>
 <td>
<strong>Figure 7: Image fusion result of SAR and optical imagery</strong>
 </td>
 <td>
 </td>
 /tr>
</table>

## ArcGIS Toolbox

ASF has developed a custom ArcGIS Toolbox for working with RTC datasets in either ArcGIS Desktop or ArcGIS Pro. It includes tools for converting between different SAR scales, calculating Log Difference, and reclassifying a raster to generate a water mask. For more information and to download the toolbox, visit our website: [https://asf.alaska.edu/how-to/data-tools/gis-tools/](https://asf.alaska.edu/how-to/data-tools/gis-tools/).

## Application Examples in the Literature

The following journal articles represent some of the work being done using Radiometric Terrain Corrected Sentinel-1 data sets.

### Crop Monitoring

Clauss, K., Ottinger M. and Kuenzer, C. 2018. Mapping rice areas with Sentinel-1 time series and superpixel segmentation. *International Journal of Remote Sensing*, **39**(5):1399-1420. DOI: [10.1080/01431161.2017.1404162](https://doi.org/10.1080/01431161.2017.1404162)

Nguyen, D.B., Gruber A. and Wagner, W. 2016. Mapping rice extent and cropping scheme in the Mekong Delta using Sentinel-1A data. *Remote Sensing Letters*, **7**(12):1209-1218. DOI: [10.1080/2150704X.2016.1225172](https://doi.org/10.1080/2150704X.2016.1225172)

### Disaster Response

Markert, K.N., Chishtie, F., Anderson, E.R., Saah, D., Griffin, R.E. 2018. On the merging of optical and SAR satellite imagery for surface water mapping applications. *Results In Physics*, **9**:275-277. DOI: [10.1016/j.rinp.2018.02.054](https://doi.org/10.1016/j.rinp.2018.02.054)

Twele, A., Cao, W., Plank, S. and Martinis, S. 2016. Sentinel-1-based flood mapping: a fully automated processing chain. *International Journal of Remote Sensing*, **37**(13):2990-3004. DOI: [10.1080/01431161.2016.1192304](https://doi.org/10.1080/01431161.2016.1192304)

### Land Classification and Change Detection

Muro, J., Canty, M., Conradsen, K., Hüttich, C., Nielsen, A.A., Skriver, H., Remy, F., Strauch, A., Thonfeld, F. and Menz, G. 2016. Short-Term change detection in wetlands using Sentinel-1 time series. *Remote Sensing*, **8**(10):795. DOI: [10.3390/rs8100795](https://doi.org/10.3390/rs8100795)

Rüetschi, M., Schaepman, M.E., Small, D. 2018. Using Multitemporal Sentinel-1 C-band backscatter to monitor phenology and classify deciduous and coniferous forests in Northern Switzerland. *Remote Sensing*, **10**(1):55. DOI: [10.3390/rs10010055](https://doi.org/10.3390/rs10010055)

## Data Access

To view or download Sentinel-1 RTC products, please see the links below:

**Vertex:** [https://search.asf.alaska.edu/](https://search.asf.alaska.edu/)

**API:** [https://asf.alaska.edu/api/](https://asf.alaska.edu/api/)

For details on accessing data, including other SAR datasets, see ASF’s Get Started guide: [https://asf.alaska.edu/how-to/get-started/](https://asf.alaska.edu/how-to/get-started/)

To access data recipes, which are step-by-step tutorials for processing and working with SAR data, see ASF’s tutorials page: [https://asf.alaska.edu/how-to/data-recipes/data-recipe-tutorials/](https://asf.alaska.edu/how-to/data-recipes/data-recipe-tutorials/)
