# Water Masking

ASF maintains a global water mask dataset for use during InSAR processing. 

Unwrapping phase differences over waterbodies can introduce unwrapping errors, resulting in misleading deformation signals. Applying a water mask to the interferogram *before* phase unwrapping can significantly improve the quality of the unwrapped interferogram, as illustrated in ASF's [InSAR Water Masking Tutorial](https://storymaps.arcgis.com/stories/485916be1b1d46889aa436794b5633cb "InSAR Water Masking StoryMap" ){target=_blank}. 

When ordering [On-Demand InSAR products from ASF](https://hyp3-docs.asf.alaska.edu/guides/insar_product_guide "ASF Sentinel-1 InSAR Product Guide" ){target=_blank}, users can choose the [option to apply the water mask](https://hyp3-docs.asf.alaska.edu/guides/insar_product_guide/#apply-water-mask "InSAR Product Guide - Processing Options - Apply Water Mask" ){target=_blank} prior to phase unwrapping. Even if users choose *not* to apply the water mask to the interferogram, a copy of the water mask is always included in the InSAR product package for reference. 

## Water Mask Dataset

ASF implemented the use of a new water mask for InSAR processing on February 15, 2024. The surface water extent datasets available from [OpenStreetMap](https://www.openstreetmap.org/about "openstreetmap.org/about" ){target=_blank} and [ESA WorldCover](https://esa-worldcover.org/en/about/about "esa-worldcover.org/en/about" ){target=_blank} were a significant improvement over the outdated version of the [Global Self-consistent, Hierarchical, High-resolution Geography](https://storymaps.arcgis.com/stories/485916be1b1d46889aa436794b5633cb#ref-n-pezhKQ "InSAR Water Masking Tutorial - GSSICB" ){target=_blank} dataset that we were using prior to this change. The data from these new sources is more recent, more detailed, and has fewer geolocation artifacts. 

The code used to generate this global water mask is available as part of the [asf_tools Python package](https://github.com/ASFHyP3/asf-tools "github.com/ASFHyP3/asf-tools" ){target=_blank}. More information on generating your own water mask using the same approach is available in the [readme file for the watermasking subpackage in the asf-tools GitHub repository](https://github.com/ASFHyP3/asf-tools/tree/develop/src/asf_tools/watermasking "asf_tools GitHub repo water masking readme" ){target=_blank}.

### Source Data

ASF's water mask uses data from both [OpenStreetMap](https://www.openstreetmap.org/about "openstreetmap.org/about" ){target=_blank} and [ESA WorldCover](https://esa-worldcover.org/en/about/about "esa-worldcover.org/en/about" ){target=_blank}. Areas within Canada, Alaska, and Russia are primarily covered by ESA WorldCover data, while the rest of the world is covered by OpenStreetMap data. 

The water mask identifies coastal waters and most inland waterbodies. All remaining pixels (land, islands in large lakes, very small inland waterbodies, and landfast Antarctic ice) are considered to be not water. 

Source data for the water mask is only available from 85°S to 85°N. Areas north of 85°N are all treated as water, and areas south of 85°S are all treated as not water.

#### OpenStreetMap (OSM)

[OpenStreetMap](https://www.openstreetmap.org/about "openstreetmap.org/about" ){target=_blank} is a crowd-sourced open-data mapping effort. The [OSM database](https://planet.openstreetmap.org/ "planet.openstreetmap.org" ){target=_blank} of geographic features can be accessed by anyone, and it includes a number of categories that can be used to map surface water extent.

OSM data was used to generate the water mask for all areas except Canada, Alaska, and Russia. To extract the relevant water extent data from the OSM database, the following filters were applied:

- wr/natural = water 
- landuse = reservoir
- waterway = *

In many cases, waterway features stretch from one bank to the other, so islands within those waterways would not be identified as land. To remove islands from the water mask extent, the following filters were applied to the extracted surface water dataset:

- place = island 
- place = islet

The resulting list of features was exported as a shapefile, then converted to raster format for inclusion in the reference water mask.

#### ESA WorldCover

In October 2021, the European Space Agency (ESA) released the first version of its global land cover dataset, [WorldCover](https://esa-worldcover.org/en/about/about "esa-worldcover.org/en/about" ){target=_blank}. It uses remote sensing data from the Sentinel-1 and Sentinel-2 missions to generate land cover classes, including water. More information is available from the [ESA WorldCover 2020 website](https://worldcover2020.esa.int/ "worldcover2020.esa.int" ){target=_blank}.

This dataset was used to generate the water masks for Canada, Alaska, and Russia. It includes one class for permanent water bodies. The version 1.0 source rasters were downloaded from the [ESA WorldCover 2020 Downloader site](https://worldcover2020.esa.int/downloader "worldcover2020.esa.int/downloader" ){target=_blank}. They were reclassified so that all areas with a value of 80 (Permanent water bodies) were defined as water, and all other values were considered not water.

## Reference Water Mask

The water mask rasters generated from the OSM and WorldCover datasets were mosaicked together, then tiled to 5° latitude by 5° longitude for storage. Because source data is only available from 85°S to 85°N, tiles were added to fill the polar areas. All pixels north of 85°N are treated as water, and all pixels south of 85°S are treated as land.

This reference dataset is stored in a public AWS S3 bucket: 

`s3://asf-dem-west/WATER_MASK/TILES/`

In the reference raster dataset hosted in AWS, pixels with surface water are assigned a value of 1, and all other pixels are assigned a value of 0. 

***Note that the pixel values used in the reference water mask are opposite to the pixel values used for the water masks included in the InSAR product packages. Refer to the [Applying the Water Mask section](#applying-the-water-mask-during-insar-processing "Jump to Applying the Water Mask during InSAR Processing section") for more information on how the reference water mask is transformed during InSAR processing.***

### Acknowledgments

#### OpenStreetMap
OpenStreetMap® is open data, licensed under the [Open Data Commons Open Database License](https://opendatacommons.org/licenses/odbl/ "opendatacommons.org/licenses/odbl" ){target=_blank} (ODbL) by the [OpenStreetMap Foundation](https://osmfoundation.org/ "osmfoundation.org" ){target=_blank} (OSMF).

#### ESA WorldCover
© ESA WorldCover project. Contains modified Copernicus Sentinel data (2020) processed by ESA WorldCover consortium.

## Applying the Water Mask during InSAR Processing

When an InSAR job is submitted for [ASF's On Demand processing](https://storymaps.arcgis.com/stories/68a8a3253900411185ae9eb6bb5283d3 "InSAR On Demand Tutorial" ){target=_blank}, the coordinates of the four corners of the input Sentinel-1 scene are used to find the water mask tile(s) that cover the scene. If the scene crosses multiple tiles, the necessary tiles are mosaicked together. The water mask is then clipped to match the spatial extent of the input Sentinel-1 scene pair.

The pixel values of the mosaicked and clipped water mask are changed to meet the requirements of the InSAR processing software. **Water pixels are assigned a value of 0, and all remaining pixels are assigned a value of 1.** *Note that these pixel values differ from the reference water mask, where water pixels have a value of 1 and all other pixels have a value of 0.*

If the option to [Apply Water Mask](https://hyp3-docs.asf.alaska.edu/guides/insar_product_guide/#apply-water-mask "InSAR Product Guide - Processing Options - Apply Water Mask" ){target=_blank} was selected by the user submitting the InSAR job, this mask is then used as an input, along with coherence values, to generate the [validity mask](https://hyp3-docs.asf.alaska.edu/guides/insar_product_guide/#masking "InSAR Product Guide - Masking" ){target=_blank} used for phase unwrapping. The 0-value water pixels are excluded from use in phase unwrapping.

A copy of the water mask is always included in the InSAR product package for reference, even if the user chose not to select the option to apply the water mask. In this copy of the water mask, the pixel values are the same as what is used in InSAR processing: pixels indicating water have a value of 0, and all other pixels are assigned a value of 1.

## Older Water Mask Versions

The first water mask that ASF used for InSAR On-Demand processing was generated using the [Global Self-consistent, Hierarchical, High-resolution Geography Database (GSHHG)](http://www.soest.hawaii.edu/wessel/gshhg/ "soest.hawaii.edu/wessel/gshhg/" ){target=_blank} dataset. 

This mask combined the GSHHG full-resolution L1 (boundary between land and ocean) and L5 (boundary between Antarctic landfast ice and ocean) datasets, and removed the L2 (boundary between land and large inland waterbodies) dataset minus the L3 (islands) dataset.

Originally, the dataset was buffered out 3 km along coastlines and 5 km along the shorelines of inland waterbodies. This buffer was included to decrease the chance that valid land pixels would be excluded from phase unwrapping due to outdated shorelines or geolocation offsets. The [discovery that the inclusion of this extra water still led to phase unwrapping errors](https://storymaps.arcgis.com/stories/485916be1b1d46889aa436794b5633cb#ref-n-sKugOV "InSAR Water Mask Tutorial - Mt. Edgecumbe" ){target=_blank} resulted in the removal of the buffer from the dataset, effective September 27, 2022. 

## Learn More

Refer to the [InSAR Water Masking Tutorial](https://storymaps.arcgis.com/stories/485916be1b1d46889aa436794b5633cb "InSAR Water Masking StoryMap" ){target=_blank} for detailed descriptions of the changes to the water mask used for InSAR processing, and interactive content illustrating the impacts these changes have had on output products. 

[![InSAR Water Masking Tutorial](images/watermask-tutorial.png "InSAR Water Masking StoryMap Tutorial")](https://storymaps.arcgis.com/stories/485916be1b1d46889aa436794b5633cb "InSAR Water Masking StoryMap Tutorial" ){target=_blank}