{% extends "guides/insar_product_guide_template.md" %}

{% block header %}
# Sentinel-1 Burst InSAR Product Guide

TODO
{% endblock %}

{% block workflow %}
## InSAR Workflow
TODO

### Pre-Processing

TODO

#### Download Bursts

The burst InSAR workflow accepts as input two
[Interferometric Wide swath Single Look Complex](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-1-sar/acquisition-modes/interferometric-wide-swath "https://sentinel.esa.int/web/sentinel/user-guides/sentinel-1-sar/acquisition-modes/interferometric-wide-swath" ){target=_blank}
(IW SLC) burst granules with the same burst ID.
The bursts are downloaded using ASF's
[Sentinel-1 Burst Extractor](https://sentinel1-burst-documentation.asf.alaska.edu/ "https://sentinel1-burst-documentation.asf.alaska.edu/" ){target=_blank}.

#### Prepare the DEM File
TODO

#### Download Orbit and Auxiliary Data Files
TODO

### InSAR Processing
TODO

### Post-Processing

#### Apply Water Mask
A water mask identifying coastal waters and major inland waterbodies is generated using the Global Self-consistent,
Hierarchical, High-resolution Geography Database (GSHHG) dataset (https://www.ngdc.noaa.gov/mgg/shorelines).

Users can optionally choose to apply the water mask to output products, which affects the wrapped interferogram,
the unwrapped interferogram, and the browse image. Areas covered by the water mask in these output images are set to
NoData.

Applying a water mask to an interferogram is only supported *after* phase unwrapping. Note that
applying the mask after phase unwrapping does not prevent unwrapping errors caused by the inclusion of water pixels
as valid data during the phase unwrapping process. When phase unwrapping occurs over large expanses of water, it can
lead to unexpected deformation signals or phase jumps in the unwrapped outputs, and the current masking approach
does not correct for these impacts.

#### Product Creation
TODO

{% endblock %}

{% block packaging %}
## Product Packaging
TODO

### Naming Convention
TODO

### Image Files
TODO

### Metadata Files
TODO

{% endblock %}
