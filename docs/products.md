# Available HyP3 Products

## RTC

SAR datasets inherently contain geometric and radiometric distortions due to terrain
being imaged by a side-looking instrument. Radiometric Terrain Correction (RTC) removes
these distortions and creates analysis-ready data suitable for use in GIS applications.
RTC processing is a required first step for many amplitude-based SAR applications.

Sentinel-1 RTC products are generated leveraging GAMMA Software. Products are 
distributed as UTM-projected GeoTIFFs with a pixel spacing of 30 meters. To learn
more, visit the
[ASF Sentinel-1 RTC Product Guide](guides/rtc_product_guide.md).

For step-by-step instructions for searching for, ordering, downloading and using On Demand RTC products, visit our [RTC On Demand!](https://storymaps.arcgis.com/stories/2ead3222d2294d1fae1d11d3f98d7c35) story map.

A Digital Elevation Model (DEM) is required for processing RTC. ASF uses the
best publicly-available DEM with full coverage of the processing area. To learn more,
visit [Digital Elevation Models](dems.md).

## InSAR

Interferometric SAR (InSAR) uses the phase differences from repeat passes over the
same area to identify regions where the distance between the sensor and the Earth's
surface has changed. This allows for the detection and quantification of deformation
or movement. To learn more, visit the [ASF Sentinel-1 RTC Product Guide](guides/rtc_product_guide.md)

Use caution when generating interferograms for areas with extensive/dense vegetation cover.
Because Sentinel-1 is a C-band sensor, the waves will not penetrate very deeply into vegetation.
Imagery of densely vegetated areas likely represents the top of the canopy rather than the
actual terrain. In addition, vegetated areas tend to have low coherence, because plants can grow
or move from one acquisition to the next.

For step-by-step instructions for searching for, ordering and downloading On Demand InSAR products, visit our [InSAR On Demand!](https://storymaps.arcgis.com/stories/68a8a3253900411185ae9eb6bb5283d3) story map.

A Digital Elevation Model (DEM) is required for processing InSAR. ASF uses the
best publicly-available DEM with full coverage of the processing area. To learn more,
visit [Digital Elevation Models](dems.md).

## autoRIFT

[AutoRIFT](https://github.com/leiyangleon/autoRIFT){target=_blank} produces a velocity map from
observed motion using a feature tracking algorithm developed as part of the 
[NASA MEaSUREs ITS_LIVE](https://its-live.jpl.nasa.gov/){target=_blank} project. To learn more,
visit the ITS_LIVE project website.

A Digital Elevation Model (DEM) is required for autoRIFT processing. ASF uses the
best publicly-available DEM with full coverage of the processing area. To learn more,
visit [Digital Elevation Models](dems.md).
