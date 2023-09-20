{% block header %}{% endblock %}

## Introduction
Interferometric Synthetic Aperture Radar (InSAR) processing uses two SAR images collected over the same area to determine geometric properties of the surface. Missions such as Sentinel-1 are [designed for](https://sentinel.esa.int/web/sentinel/missions/sentinel-1/mission-objectives "https://sentinel.esa.int/web/sentinel/missions/sentinel-1/mission-objectives" ){target=_blank} monitoring surface deformation using InSAR, which is optimal when acquisitions are made from a consistent location in space ([short perpendicular baseline](#baselines "Jump to Baselines section of this document")) over regular time intervals.

The phase measurements of two SAR images acquired at different times from the same place in orbit are differenced to detect and quantify surface changes, such as deformation caused by earthquakes, volcanoes, or groundwater subsidence.

InSAR can also be used to generate digital elevation models, but the optimal mission for DEM generation has the opposite characteristics of the Sentinel-1 mission. Topography is best mapped when the two acquisitions are obtained as close together as possible in time ([short temporal baseline](#baselines "Jump to Baselines section of this document")), but from different vantage points in space (larger perpendicular baseline than would be optimal for deformation mapping).

### Brief Overview of InSAR
SAR is an active sensor that transmits pulses and listens for echoes. These echoes are recorded in phase and amplitude, with the phase being used to determine the distance from the sensor to the target and the amplitude yielding information about the roughness and dielectric constant of that target.

![Figure 1](../images/phase_diff.png "Difference in range shows movement of the surface imaged")

*Figure 1: Two passes of an imaging SAR taken at time T<sub>0</sub> and T<sub>0</sub> + ∆t, will give two distances to the ground, R<sub>1</sub> and R<sub>2</sub>.  A difference between R<sub>1</sub> and R<sub>2</sub> shows motion on the ground.  In this case, a subsidence makes R<sub>2</sub> greater than R<sub>1</sub>.  Credit: [TRE ALTAMIRA](https://site.tre-altamira.com/insar/ "https://site.tre-altamira.com/insar" ){target=_blank}*

InSAR exploits the phase difference between two SAR images to create an interferogram that shows where the phase and, therefore, the distance to the target has changed from one pass to the next, as illustrated in Figure 1.  There are several factors that influence the interferogram, including earth curvature, topographic effects, atmospheric delays, surface motion, and noise.  With proper processing, Sentinel-1 InSAR can be used to detect changes in the earth's surface down to the centimeter scale. Applications include volcanic deformation, subsidence, landslide detection, and earthquake assessment.

### Wavelengths
The SAR sensors on the Sentinel-1 satellites transmit C-band signals, with a wavelength of 5.6 cm. The signal wavelength impacts the penetration capability of the signal, so it is important to be aware of the sensor wavelength when working with SAR datasets. C-band SAR will penetrate more deeply into canopy or surfaces than an X-band signal, but not nearly as deep as an L-band SAR signal, which, with a wavelength on the order of 25 cm, is better able to penetrate canopy and return signals from the forest floor.

Different wavelengths are also sensitive to different levels of deformation. To detect very small changes over relatively short periods of time, you may require a signal with a smaller wavelength (such as X-band). However, signals with shorter wavelengths are also more prone to decorrelation due to small changes in surface conditions such as vegetation growth.

For slower processes that require a longer time interval to detect movement, longer wavelengths (such as L-band) may be necessary. C-band sits in the middle. It can detect fairly small changes over fairly short periods of time, but is not as sensitive to small changes as X-band or as able to monitor surface dynamics under canopy as L-band.

### Polarizations
Polarization refers to the direction of travel of an electromagnetic wave.  A horizontal wave is transmitted so that it oscillates in a plane parallel to the surface imaged, while a vertical wave oscillates in a plane perpendicular to the surface imaged.

Most modern SAR systems can transmit chirps with either a horizontal or vertical polarization. In addition, some of these sensors can listen for either horizontal or vertical backscatter. This gives rise to 4 different types of returns: HH, HV, VV, and VH, with the first letter indicating the transmission method and the second the receive method. For example, VH is a vertically polarized transmit signal with horizontally polarized echoes recorded.

For InSAR applications, processing is generally performed on the co-pol (VV or HH) data and not on the cross-pol (VH or HV) data. Also, each image used in an InSAR pair is required to be the same polarization - two HH images of the same area could form a valid pair, while a single HH with a single VV of the same area would not.

### Baselines
#### Perpendicular Baseline
The term *baseline* refers to the physical distance between the two vantage points from which images used as an InSAR pair are acquired. The baseline is decomposed into perpendicular (also called normal) and parallel components, as shown in Figure 2.

To monitor surface deformation, the perpendicular baseline for the two acquisitions should be very small in order to maximize the coherence of the phase measurements.

In order to determine topography, two slightly different vantage points are required. Sensitivity to topography depends on the perpendicular baseline, the sensor wavelength, the distance between the satellite and the ground, and the sensor look angle.

![Figure 2](../images/baseline_asf.png "Geometry of InSAR Baselines.")

*Figure 2: Geometry of InSAR baselines. Two satellite passes image the same area on the ground from positions S<sub>1</sub> and S<sub>2 </sub>, resulting in a baseline of B, which can be decomposed into ****perpendicular**** (B<sub>⟂ </sub>) and ****parallel**** (B<sub>∥ </sub>) components. Here Y is the direction of travel, referred to as the ****along-track**** or ****azimuth**** direction, and X is the direction perpendicular to motion, referred to as the ****cross-track**** or ****range**** direction. Credit: ASF*

#### Temporal Baseline
In contrast to the (physical) baseline, the *temporal baseline* refers to the time separation between imaging passes. Along-track interferometry measures motion in the millisecond to second range. This technique can detect ocean currents and rapidly moving objects like boats. Differential interferometry is the standard method used to detect motion in the range of days to years. This is the type of interferometry that is performed by the Sentinel-1 HyP3 InSAR processing algorithm. Table 1 lists different temporal baselines, their common names, and what they can be used to measure.

| Duration      | Known as     | Measurement of                                                      | 
|---------------|--------------|---------------------------------------------------------------------|
| ms to sec     | along-track  | ocean currents, moving object detection, MTI                        | 
| days          | differential | glacier/ice fields/lava flows, surface water extent, hydrology      |
| days to years | differential | subsidence, seismic events, volcanic activity, crustal displacement | 

*Table 1: Temporal baselines and what they measure. Different geophysical phenomena can be detected based upon the temporal baseline. In general, the longer the temporal baseline, the smaller the motion that can be detected.*

#### Critical Baseline
Large baselines are better than small for topographic mapping. However, as the baseline increases, coherence decreases. At some point, it is impossible to create an interferogram because of baseline decorrelation. The maximum viable baseline per platform, referred to as the *critical baseline*, is a function of the distance to the ground, the wavelength, and the viewing geometry of the platform.

For Sentinel-1, this critical baseline is about 5 km. In practice, if the perpendicular baseline between images is more than 3/4 of the critical baseline, interferogram creation will be problematic due to the level of noise.

For deformation mapping, it is best to minimize the perpendicular baseline whenever possible, but there may be tradeoffs in terms of finding suitable temporal baselines. In most cases, however, pairs selected for deformation mapping will have perpendicular baselines *much* smaller than the critical baseline.

## Ordering On Demand InSAR Products
All of ASF's On Demand InSAR products are generated using ASF's HyP3 platform. Jobs can be submitted for processing using the [Vertex](https://search.asf.alaska.edu/ "https://search.asf.alaska.edu" ){target=_blank} data portal, the [HyP3 Python SDK](https://hyp3-docs.asf.alaska.edu/using/sdk/ "https://hyp3-docs.asf.alaska.edu/using/sdk" ){target=_blank} or the [HyP3 API](https://hyp3-docs.asf.alaska.edu/using/api/ "https://hyp3-docs.asf.alaska.edu/using/api" ){target=_blank}.

### Vertex
InSAR pairs are selected in [Vertex](https://search.asf.alaska.edu/#/ "https://search.asf.alaska.edu" ){target=_blank} using either the [Baseline Search](https://docs.asf.alaska.edu/vertex/baseline/ "https://docs.asf.alaska.edu/vertex/baseline" ){target=_blank} or the [SBAS Search](https://docs.asf.alaska.edu/vertex/sbas/ "https://docs.asf.alaska.edu/vertex/sbas" ){target=_blank} interface. The process of selecting pairs is the same for both SLCs and bursts, but you will need to select the appropriate dataset when searching for content. As illustrated below, select the **Sentinel-1** option in the Dataset menu to search for SLCs, and select the **S1 Bursts** option to search for bursts. 

![Vertex Dataset Selection](../images/vertex-dataset-selection.png)

The [Baseline](https://docs.asf.alaska.edu/vertex/baseline/ "https://docs.asf.alaska.edu/vertex/baseline" ){target=_blank} tool is the best option for selecting a specific single InSAR pair. Use the [Geographic Search](https://docs.asf.alaska.edu/vertex/manual/#geographic-search-options "https://docs.asf.alaska.edu/vertex/manual/#geographic-search-options" ){target=_blank} to find an image that covers your time and area of interest, select that item in the results, and click the Baseline button in the center panel. The Baseline tool then displays all of the scenes that could be used to generate an interferogram using the selected image. Scroll through the results to find pairs to add to the On Demand queue, or click on items displayed in the plot to highlight that particular image pair.

The [SBAS](https://docs.asf.alaska.edu/vertex/sbas/ "https://docs.asf.alaska.edu/vertex/sbas" ){target=_blank} tool is designed for generating time series of InSAR pairs. As with the Baseline search, you can launch the SBAS search from the center panel of a [Geographic Search](https://docs.asf.alaska.edu/vertex/manual/#geographic-search-options "https://docs.asf.alaska.edu/vertex/manual/#geographic-search-options" ){target=_blank} result. It will display all of the valid InSAR pairs through time based on the acquisition location of the input scene. This functionality is designed for processing a series of interferograms to be used in SBAS (Small BAseline Subset) analysis. The results can be adjusted based on baseline criteria (both perpendicular and temporal), and restricted to specific periods of time. Once the list is refined, you have the option to add all of the InSAR pairs displayed in the results to the On Demand queue.

### HyP3 SDK and API
The [HyP3 SDK](https://hyp3-docs.asf.alaska.edu/using/sdk/ "https://hyp3-docs.asf.alaska.edu/using/sdk" ){target=_blank} provides support for processing nearest-neighbor interferograms for a selected granule. Specifying nearest-neighbor processing will find the next appropriate scene back in time to use as the reference granule for generating an interferogram with the selected granule. You can specify up to 2 nearest neighbors, which will pair the scene closest in time and next-closest in time to the selected granule for generating InSAR products, as demonstrated in this [sample HyP3 SDK Jupyter Notebook](https://nbviewer.jupyter.org/github/ASFHyP3/hyp3-sdk/blob/main/docs/sdk_example.ipynb#Submitting-Sentinel-1-InSAR-jobs "https://nbviewer.jupyter.org/github/ASFHyP3/hyp3-sdk/blob/main/docs/sdk_example.ipynb#Submitting-Sentinel-1-InSAR-jobs" ){target=_blank}.

You may still find the Geographic, Baseline and SBAS searches in Vertex useful for finding reference scenes or picking specific pairs to use when submitting InSAR jobs via the [SDK](https://hyp3-docs.asf.alaska.edu/using/sdk/ "https://hyp3-docs.asf.alaska.edu/using/sdk" ){target=_blank} or [API](https://hyp3-docs.asf.alaska.edu/using/api/ "https://hyp3-docs.asf.alaska.edu/using/api" ){target=_blank}.

### Considerations for Selecting an InSAR Pair
When selecting an InSAR pair, observe the following required conditions:

1. Images from an identical orbit direction (either ascending or descending)
2. Images with identical incidence angles and beam mode
3. Images with identical resolution and wavelength (usually from the same sensor)
4. Images with the same viewing geometry (same path and frame)
5. Images with identical polarizations (both HH or VV)

In addition, the following suggestions may be helpful:

1. Use images from similar seasons/growth/weather conditions
2. For deformation mapping: limited spatial separation of acquisition locations (small physical baseline)
3. For topographic mapping: limited time separation between images (small temporal baseline)

To analyze deformation caused by a single discrete event, such as an earthquake, select images that bracket the event as closely in time as possible. Keeping the window narrowly focused on the time of the event will reduce the impacts of other processes that may mask the signal of the event of interest.

{% block processing_options %}{% endblock %}

{% block workflow %}{% endblock %}

{% block packaging %}{% endblock %}

## Limitations
### Baseline Calculation
The baseline is defined as the difference of the platform positions when a given area is imaged. HyP3 baselines are calculated using the best state vectors available. If precise orbits are not yet available for the input granules, restituted orbits will be used. The original predicted orbits are not used for InSAR processing in HyP3. **If no restituted or precise state vectors are available, the process will not run.**

### Coherence
The phase measurements in the two images used in InSAR must be coherent in order to detect change. Random changes in phase from one acquisition to the next can mask actual surface deformation. Vegetation is a common driver of decorrelation, as changes can easily take place in the interval between two acquisitions due to growth, seasonal changes, or wind effects. It will be difficult to generate valid interferograms with C-band data in heavily vegetated regions due to lack of coherence even with fairly short time intervals.

Consider seasonality when selecting image pairs. Decorrelation can be particularly high when comparing phase from different seasons. Changes in the condition of vegetation (especially deciduous canopies), snow, moisture, or freeze/thaw state can impact phase measurements. In cases where a temporal baseline is required that spans seasons, it may be better to use an annual interferogram if possible so that the images are more comparable in terms of seasonality.

### Line-of-Sight Measurements
When looking at a single interferogram, the deformation measurements in the line-of-sight orientation of the sensor indicate relative motion towards or away from the sensor. InSAR is not sensitive to motion in the azimuth direction of the satellite, so motion that occurs in the same direction as the satellite's direction of travel will not be detected.

A single interferogram cannot be used to determine the relative contributions of vertical and horizontal movement to the line-of-sight displacement measurement. The vertical displacement map is generated based on the assumption that the movement is entirely in the vertical direction, which may not be realistic for some processes. To determine how much of the signal is driven by vertical vs. horizontal movement, you must either use a time series of interferograms, or use reference measurements with known vertical and horizontal components (such as GNSS measurements from the region of deformation) to deconstruct the line-of-sight displacement.

All displacement values are calculated relative to a [reference point](#phase-unwrapping-reference-point "Jump to Phase Unwrapping Reference Point part of Limitations section in this document"), which may or may not be an appropriate benchmark for measuring particular areas of displacement within the interferogram.

### Phase Unwrapping Reference Point
The reference point for phase unwrapping is set to be the location of the pixel with the highest coherence value. As described in the [phase unwrapping section](#reference-point "Jump to Reference Point section of this document"), this may not always be an ideal location to use as a reference point. If it is located in an area undergoing deformation, or in a patch of coherent pixels that is separated from the area undergoing deformation by a gap of incoherent pixels, the unwrapping may be of lower quality than if the reference point was in a more suitable location.

Even when there are not phase unwrapping errors introduced by phase discontinuities, it is important to be aware that unwrapped phase differences and displacement values are all calculated relative to the reference point. The phase difference value of the reference point is set to 0 during phase unwrapping, so any displacement values will be relative to that benchmark. If the location of the default reference point is in the middle of an area that underwent deformation, displacement values may be different than expected.

If you are interested in the amount of displacement in a particular area, you may wish to choose your own reference point. The ideal reference point would be in an area of high coherence beyond where deformation has occurred. The unwrapped phase measurements can be adjusted to be relative to this new reference point, and displacement values can be recalculated accordingly. To adjust the values in the unwrapped phase GeoTIFF, simply select a reference point that is optimal for your use case and subtract the unwrapped phase value of that reference point from each pixel in the unwrapped phase raster:

**ΔΨ<sup>&ast;</sup>** = **ΔΨ** - Δψ<sub>ref</sub>

where **ΔΨ<sup>&ast;</sup>** is the adjusted unwrapped phase, **ΔΨ** is the original unwrapped phase, and Δψ<sub>ref</sub> is the unwrapped phase value at the new reference point.

#### Impacts on Displacement Measurements
The measurements in the displacement maps are calculated from the unwrapped phase values, so will similarly be impacted by the location of the reference point. You may wish to recalculate the displacement values relative to a new reference point. The approach for correcting the displacement maps will be different for the line-of-sight and vertical measurements.

##### Correcting Line-of-Sight Displacement Maps
If you have already corrected the unwrapped phase raster, you can calculate a new line-of-sight (LOS) displacement map by applying the following calculation on a pixel-by-pixel basis using the unwrapped phase GeoTIFF:

**ΔΩ<sup>&ast;</sup>** = - **ΔΨ<sup>&ast;</sup>** λ / 4π

where **ΔΩ<sup>&ast;</sup>** is the adjusted line-of-sight displacement in meters, **ΔΨ<sup>&ast;</sup>** is the [adjusted unwrapped phase](#phase-unwrapping-reference-point "Jump to Phase Unwrapping Reference Point part of Limitations section in this document"), and λ is the wavelength of the sensor in meters (0.055465763 for Sentinel-1).

Setting the **ΔΨ<sup>&ast;</sup>** value to be negative reverses the sign so that the difference is relative to the earth rather than the sensor. A positive phase difference value indicates subsidence, which is unintuitive when thinking about movement on the earth's surface. Applying the negative will return positive displacement values for uplift and negative values for subsidence.

If you are not interested in adjusted unwrapped phase values, you can also directly correct the LOS Displacement map included optionally in the InSAR product package:

**ΔΩ<sup>&ast;</sup>** = **ΔΩ** - Δω<sub>ref</sub>

where **ΔΩ<sup>&ast;</sup>** is the adjusted line-of-sight displacement in meters, **ΔΩ** is the original line-of-sight displacement in meters, and Δω<sub>ref</sub> is the line-of-sight displacement value at the new reference point.

##### Correcting Vertical Displacement Maps
Vertical displacement maps cannot be adjusted directly, and must be recalculated from the adjusted unwrapped phase image. You will also need the θ look vector map (lv_theta GeoTIFF) for this calculation. The look vector maps are not included in the InSAR product package by default; the option to Include Look Vectors must be selected when ordering the product.

To calculate an adjusted vertical displacement raster, calculate the [adjusted unwrapped phase](#phase-unwrapping-reference-point "Jump to Phase Unwrapping Reference Point part of Limitations section in this document"), then apply the following:

**Δϒ<sup>&ast;</sup>** = - **ΔΨ<sup>&ast;</sup>** λ cos(½π - ***LV*<sub>θ</sub>**) / 4π

where **Δϒ<sup>&ast;</sup>** is the adjusted vertical displacement in meters, **ΔΨ<sup>&ast;</sup>** is the adjusted unwrapped phase, λ is the wavelength of the sensor in meters (0.055465763 for Sentinel-1), and ***LV*<sub>θ</sub>** is the theta look vector (from the lv_theta GeoTIFF).

As with the LOS Displacement maps, setting the **ΔΨ<sup>&ast;</sup>** value to be negative reverses the sign so that the difference is relative to the earth rather than the sensor. Applying the negative will return positive displacement values for uplift and negative values for subsidence.

#### Displacement Values from a Single Interferogram

In general, calculating displacement values from a single interferogram is not recommended. While the displacement rasters provided with ASF's On Demand InSAR products can be helpful in visualizing changes, we do not recommend that you rely on a single interferogram when coming to conclusions about surface displacement, even if you apply a correction based on a manually selected reference point. It will be more robust to use a time series approach to more accurately determine the pattern of movement. When using SAR time-series software such as [MintPy](https://mintpy.readthedocs.io/en/latest/ "https://mintpy.readthedocs.io/en/latest" ){target=_blank}, you have the option to select a specific reference point, and the values of the input rasters will be adjusted accordingly.

## Error Sources
On Demand InSAR products do not currently correct for some common sources of error in interferometry, such as atmospheric effects. Further processing or time series analysis can be performed by the user to identify or reduce the impact of some of these errors when using On Demand InSAR products for analysis.

### Atmospheric Delay
While SAR signals can penetrate clouds, atmospheric conditions can delay the transmission of the signal. This results in phase differences that can look like surface deformation signals but are actually driven by differences in the atmospheric conditions between the pair of acquisitions used to generate the interferogram.

In some cases, atmospheric errors can be corrected by using an atmospheric model to remove the impacts of the turbulent delay from the interferogram. Another approach is to use time series analysis to identify outliers.

***Always doubt your interferogram first!*** View the interferogram critically, and consider if fringe patterns could potentially be driven by atmospheric effects. In general, it is best to avoid drawing conclusions from the outcome of a single interferogram.

#### Turbulent Delay
These delays are generally caused by differences in water vapor distribution from one image to the next. They often manifest as wobbly or sausage-shaped fringes, and can potentially mask the signal of a small earthquake.

#### Stratified Delay
This type of delay is driven mostly by pressure and temperature differences or gradients through the atmospheric column, and often correlates with topography. This atmospheric signature can be confused with movement caused by volcanic activity. If there are multiple volcanoes in an image and they all exhibit similar patterns, it is likely being driven by this type of atmospheric delay.

### DEM Errors
A DEM is used to remove topographic phase impacts, but if there are inaccuracies in the DEM, residual impacts of those errors can remain in the interferogram.

### Orbit Uncertainties
This is generally not an issue for Sentinel-1 data, as the orbits are very precise and generally reliable. On Demand InSAR products are only processed once [restituted or precise orbits](#baseline-calculation "Jump to Baseline Calculation section of this document") are available. Orbit uncertainties are more problematic when working with datasets from older missions.
