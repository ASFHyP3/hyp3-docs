# Available HyP3 Products

On-demand SAR products generated using HyP3 are currently available for the 
[Sentinel-1 mission](sentinel1.md "Sentinel-1 Mission") 
only. Unless otherwise noted, On-Demand products are available for 14 days after they have been processed.

A Digital Elevation Model (DEM) is required to generate each of the On-Demand products offered by ASF, and we 
generally use the 
[GLO-30 Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM "Copernicus DEM" ){target=_blank} 
in our processing workflows. For more information, refer to our 
[Digital Elevation Models](dems.md "HyP3 DEM Documentation") 
documentation.

## RTC

SAR datasets inherently contain geometric and radiometric distortions due to terrain
being imaged by a side-looking instrument. Radiometric Terrain Correction (RTC) removes 
these distortions and creates analysis-ready data suitable for use in GIS applications.
RTC processing is a required first step for many amplitude-based SAR applications.

Sentinel-1 RTC products are generated from Level-1 Sentinel-1 IW acquisitions (either GRD or SLC files), leveraging 
[GAMMA Software](https://gamma-rs.ch/gamma-software){target=_blank}. 
Products are distributed as GeoTIFFs projected to a UTM Zone, with a pixel spacing of 
[10, 20, or 30 meters](guides/rtc_product_guide.md#pixel-spacing "RTC Pixel Spacing Documentation"). 
Users can choose to output the products in 
[gamma-0 or sigma-0 radiometry](guides/rtc_product_guide.md#radiometry "RTC Radiometry Documentation"), 
and in 
[power, amplitude, or dB scale](guides/rtc_product_guide.md#scale "RTC Scale Documentation"). 
Users also have the option to 
[apply a speckle filter](guides/rtc_product_guide.md#speckle-filter "RTC Speckle Filter Documentation"). 
To learn more, refer to the [Sentinel-1 RTC Product Guide](guides/rtc_product_guide.md 
"Sentinel-1 RTC Product Guide").

For step-by-step instructions on searching for, ordering, downloading and using On-Demand RTC products, visit our 
[RTC On Demand!](https://storymaps.arcgis.com/stories/2ead3222d2294d1fae1d11d3f98d7c35 "RTC On Demand! StoryMap" ){target=_blank} 
tutorial.

## InSAR

Interferometric SAR (InSAR) uses the phase differences from repeat passes over the 
same area to identify regions where the distance between the sensor and the Earth's 
surface has changed. This allows for the detection and quantification of surface 
deformation or ground movement. 

There are three different processing approaches available for generating On-Demand InSAR products from Sentinel-1: 

  - [Full-scene processing using GAMMA software](#full-scene-insar-gamma) 
  - [Burst-based processing using ISCE2 software](#burst-based-insar-isce2)
  - [ARIA Frame-based processing using ISCE2 software](#aria-sentinel-1-gunw-products-isce2)

### Full-scene InSAR (GAMMA)

These products take Sentinel-1 IW SLC scene pairs as input, and processing is performed using 
[GAMMA Software](https://gamma-rs.ch/gamma-software){target=_blank}. 
Products are packaged as a collection of GeoTIFFs in a zip file. They are projected to the appropriate UTM Zone for 
the product location and can be generated at a pixel spacing of either 80 or 40 meters. To learn more, refer to the 
[Sentinel-1 InSAR Product Guide](guides/insar_product_guide.md "Sentinel-1 InSAR Product Guide").

For step-by-step instructions on searching for, ordering and downloading On Demand InSAR products, visit our [InSAR On Demand!](https://storymaps.arcgis.com/stories/68a8a3253900411185ae9eb6bb5283d3 "InSAR On Demand! StoryMap" ){target=_blank} tutorial.

### Burst-based InSAR (ISCE2)

These products take sets of individual 
[SLC bursts](https://storymaps.arcgis.com/stories/88c8fe67933340779eddef212d76b8b8 "Sentinel-1 Bursts StoryMap" ){target=_blank} 
extracted from Sentinel-1 IW SLC products as input, and processing is performed using 
[ISCE2 software](https://github.com/isce-framework/isce2#readme "https://github.com/isce-framework/isce2" ){target=_blank}. Products are packaged as a collection of 
GeoTIFFs in a zip file. They are projected to the appropriate UTM Zone for the product 
location, and can be generated at a pixel spacing of 80, 40, or 20 meters. 

The advantage of using burst-based processing is that users have more control of the extent of the output 
interferogram, and the burst footprints always fully overlap from one acquisition to the next. Users can select 
sets of up to 15 contiguous along-track bursts to generate a single output interferogram. Refer to the 
[Sentinel-1 Burst InSAR Product Guide](guides/burst_insar_product_guide.md "Sentinel-1 Burst InSAR Product Guide") 
for more information.

For step-by-step instructions on searching for, ordering and downloading On Demand Burst InSAR products, visit our 
[Burst-Based InSAR for Sentinel-1 On Demand](https://storymaps.arcgis.com/stories/191bf1b6962c402086807390b3ce63b0 "Burst-Based InSAR for Sentinel-1 On Demand StoryMap" ){target=_blank} 
tutorial.

### ARIA Sentinel-1 GUNW Products (ISCE2)

There is an extensive archive of 
[ARIA S1 GUNW](https://aria.jpl.nasa.gov/products/standard-displacement-products.html "https://aria.jpl.nasa.gov" ){target=_blank} 
(Geocoded Unwrapped Interferogram) products 
[available from ASF](https://search.asf.alaska.edu/#/?maxResults=1000&dataset=SENTINEL-1%20INTERFEROGRAM%20(BETA) "Vertex search for ARIA S1 GUNW" ){target=_blank}, 
but they are only generated in specific geographic locations. If the existing archive does not provide the 
products you need, you can generate ARIA GUNW products on demand. 

ARIA S1 GUNW products are delivered as netCDF files with 90-m pixel spacing. The On-Demand 
products are generated using the same 
[ISCE2](https://github.com/isce-framework/isce2#readme "https://github.com/isce-framework/isce2" ){target=_blank}-based 
code used to generate the archived products, and standard ARIA S1 GUNW products 
generated on demand are automatically added to the archive. This allows all users to access the On-Demand products 
indefinitely, which is an exception to the 14-day availability period that applies to all other On-Demand products.

The ARIA S1 GUNW products use a set [framing system](guides/gunw_product_guide.md#aria-frame-ids "ARIA Sentinel-1 GUNW 
Product Guide: ARIA Frame IDs") to select consistent bursts from input Sentinel-1 IW SLCs to generate interferograms. 
Refer to the 
[ARIA Sentinel-1 GUNW Product Guide](guides/gunw_product_guide.md "ARIA Sentinel-1 GUNW Product Guide") 
for more information.

## autoRIFT

[AutoRIFT](https://github.com/leiyangleon/autoRIFT "https://github.com/leiyangleon/autoRIFT" ){target=_blank} 
produces a velocity map from observed motion using a feature tracking algorithm developed as part of the 
[NASA MEaSUREs ITS_LIVE](https://its-live.jpl.nasa.gov/ "https://its-live.jpl.nasa.gov" ){target=_blank} 
project. 

To learn more, visit the 
[ITS_LIVE project website](https://its-live.jpl.nasa.gov/ "https://its-live.jpl.nasa.gov" ){target=_blank}.
