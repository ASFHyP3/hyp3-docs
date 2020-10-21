# Available HyP3 Products

## RTC

SAR datasets inherently contain geometric and radiometric distortions due to terrain
being imaged by a side-looking instrument. Radiometric terrain correction (RTC) removes
these distortions and creates analysis-ready data suitable for use in GIS applications.
RTC processing is a required first step for many amplitude-based SAR applications.

Sentinel-1 RTC products are generated leveraging GAMMA Software.  Products are 
distributed as UTM-projected GeoTIFFs with a pixel spacing of 30 meters. To learn
more, visit the
[ASF Sentinel-1 RTC Product Guide](guides/rtc_product_guide.md).

A Digital Elevation Model (DEM) is required for processing RTC. ASF uses the
best publicly-available DEM with full coverage of the processing area. To learn more,
visit [Digital Elevation Models](dems.md).

## InSAR (SDK + API only)

Interferometric SAR (InSAR) uses the phase differences from repeat passes over the
same area to identify regions where the distance between the sensor and the Earth's
surface has changed. This allows for the detection and quantification of deformation
or movement.

Use caution when generating interferograms for areas with extensive/dense vegetation cover.
Because Sentinel-1 is a C-band sensor, the waves will not penetrate very deeply into vegetation.
Imagery of densely vegetated areas likely represents the top of the canopy rather than the
actual terrain. In addition, vegetated areas tend to have low coherence, because plants can grow
or move from one acquisition to the next.

A Digital Elevation Model (DEM) is required for processing InSAR. ASF uses the
best publicly-available DEM with full coverage of the processing area. To learn more,
visit [Digital Elevation Models](dems.md).

## autoRIFT (SDK + API only)

[AutoRIFT](https://github.com/leiyangleon/autoRIFT) produces a velocity map from
observed motion using a feature tracking algorithm developed as part of the 
[NASA MEaSUREs ITS_LIVE](https://its-live.jpl.nasa.gov/) project. To learn more,
visit the ITS_LIVE project website.

A Digital Elevation Model (DEM) is required for autoRIFT processing. ASF uses the
best publicly-available DEM with full coverage of the processing area. To learn more,
visit [Digital Elevation Models](dems.md).

## Product usage guidelines

When using this data in a publication or presentation, we ask that you include the
acknowledgement provided with each product. DOIs are also provided for citation
when discussing the HyP3 software or plugins.

- For multi-file products, the acknowledgement and relevant DOIs are included in
  the `*.README.md.txt` file.
- For netCDF products, the acknowledgement is included in the `source` global attribute
  and the DOIs are included in the `references` global attribute.
