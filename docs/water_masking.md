# Water Mask

ASF maintains a global water mask dataset to use during InSAR processing. 

Unwrapping phase differences over waterbodies can introduce unwrapping errors, resulting in misleading deformation signals. Applying a water mask to the data *before* phase unwrapping can significantly improve the quality of the unwrapped interferogram, as illustrated in this [InSAR Water Masking Tutorial](https://storymaps.arcgis.com/stories/485916be1b1d46889aa436794b5633cb 'InSAR Water Masking StoryMap' ){target=_blank}. 

When ordering InSAR products On Demand from ASF, users can choose the [option to apply the water mask](https://hyp3-docs.asf.alaska.edu/guides/insar_product_guide/#apply-water-mask 'InSAR Product Guide - Processing Options - Apply Water Mask' ){target=_blank} prior to phase unwrapping. Even if users do not choose to apply this option, there is always a copy of the water mask included in the InSAR product package for reference. 

## Water Mask Dataset

ASF implemented the use of a new water mask for InSAR processing on February 15, 2024. The surface water extent data available from OpenStreetMap and ESA WorldCover were a significant improvement over the outdated version of the [Global Self-consistent, Hierarchical, High-resolution Geography](https://storymaps.arcgis.com/stories/485916be1b1d46889aa436794b5633cb#ref-n-pezhKQ 'InSAR Water Masking Tutorial - GSSICB' ){target=_blank} dataset that we were using prior to this change. The data is more recent, more detailed, and has fewer geolocation artifacts. 

### Source Data

ASF's water mask uses data from both [OpenStreetMap](https://www.openstreetmap.org/about 'https://www.openstreetmap.org/about' ){target=_blank} and [ESA WorldCover](https://esa-worldcover.org/en/about/about 'https://esa-worldcover.org/en/about/about' ){target=_blank}. Areas within Canada, Alaska, and Russia are primarily covered by ESA WorldCover data, while the rest of the world is covered by OpenStreetMaps data. 

The water mask identifies coastal waters and most inland waterbodies. All remaining pixels (land, islands in large lakes, very small inland waterbodies, and landfast Antarctic ice) are considered to be not water. Source data for the water mask is only available from 85°S to 85°N. Areas north of 85°N are all treated as water, and areas south of 85°S are all treated as not water.

The code used to generate this global watermask is available as part of the [asf_tools python library](https://github.com/ASFHyP3/asf-tools 'https://github.com/ASFHyP3/asf-tools' ){target=_blank}. More information on generating your own water mask using the same approach is available in the [asf_tools github repository](https://github.com/ASFHyP3/asf-tools/tree/develop/src/asf_tools/watermasking 'asf_tools GitHub repo watermasking readme' ){target=_blank}.

#### OpenStreetMap (OSM)

[OpenStreetMap](https://www.openstreetmap.org/about 'https://www.openstreetmap.org/about' ){target=_blank} is a crowd-sourced open-data mapping effort. The [OSM database](https://planet.openstreetmap.org/ 'https://planet.openstreetmap.org/' ){target=_blank} of geographic features can be accessed by anyone, and it includes a number of categories that can be used to map surface water extent.

OSM data was used to generate the water mask for all areas except Canada, Alaska, and Russia. To extract the relevant water extent data from the OSM database, the following filters were applied:
- wr/natural = water 
- landuse = reservoir
- waterway = *

In many cases, waterway features stretch from one bank to the other, so islands within those waterways would not be identified as land. To remove islands from the water mask extent, the following filters were applied to the extracted surface water dataset:
- place = island 
- place = islet

The resulting list of features was exported as a shapefile, then converted to raster format for inclusion in the reference water mask.

#### ESA WorldCover

In October 2021, the European Space Agency (ESA) released the first version of its global land cover dataset, [WorldCover](https://esa-worldcover.org/en/about/about 'https://esa-worldcover.org/en/about' ){target=_blank}. It uses remote sensing data from the Sentinel-1 and Sentinel-2 missions to generate land cover classes, including water. More information is available from the [ESA WorldCover 2020 website](https://worldcover2020.esa.int/ 'https://worldcover2020.esa.int/' ){target=_blank}.

This dataset was used to generate the water masks for Canada, Alaska, and Russia. It includes one class for permanent water bodies. The version 1.0 source rasters were downloaded from the [ESA WorldCover 2020 Downloader site](https://worldcover2020.esa.int/downloader 'https://worldcover2020.esa.int/downloader' ){target=_blank}. They were reclassified so that all areas with a value of 80 (Permanent water bodies) were defined as water, and all other values were considered not water.

## Reference Water Mask

The water mask rasters generated from the OSM and WorldCover datasets were mosaicked together, then tiled to 5° latitude by 5° longitude for storage. 

The water mask identifies coastal waters and most inland waterbodies. All remaining pixels (land, islands, very small inland waterbodies, and landfast Antarctic ice) are considered to be not water. 

Source data for the water mask is only available from 85°S to 85°N. Areas north of 85°N are all treated as water, and areas south of 85°S are all treated as not water.

ASF currently maintains a global water mask raster, tiled to 5x5 degrees. This reference dataset is stored in a public AWS S3 bucket: `s3://asf-dem-west/WATER_MASK/TILES/`.

In the reference raster dataset hosted in AWS, pixels with surface water are assigned a value of 1, and all other pixels are assigned a value of 0. *Note that this convention is opposite to the pixel values used for the water masks included in the InSAR product packages.* Refer to the [next section](#applying-the-water-mask-during-insar-processing) for more information. 

## Applying the Water Mask during InSAR Processing

When an InSAR job is submitted for [ASF's On Demand processing](https://storymaps.arcgis.com/stories/68a8a3253900411185ae9eb6bb5283d3 'InSAR On Demand Tutorial' ){target=_blank}, the coordinates of the four corners of the input Sentinel-1 scene are used to find the water mask tiles that cover the scene. If the scene crosses multiple tiles, the necessary tiles are mosaicked together. The water mask is then clipped to match the spatial extent of the input Sentinel-1 scene.

The values of the source water mask are defined to meet the requirements of the InSAR processing software. Water pixels are set to a value of 0, and all remaining pixels are set to a value of 1. 

If the option to Apply Water Mask was selected by the user submitting the InSAR job, this mask is then used as an input, along with coherence values, to generate the  validity mask  used for phase unwrapping. The 0-value water pixels are excluded from use in phase unwrapping.

A copy of the water mask is always included in the InSAR product package for reference, even if the user chose not to select the option to apply the water mask. In this copy of the water mask, the pixel values are the same as what is used in InSAR processing: pixels indicating water have a value of 0, and all other pixels are assigned a value of 1.
