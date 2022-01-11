# Introduction to SAR
---------------------

## How SAR Operates

SAR is an active sensor that transmits pulses and listens for echoes, called backscatter. The backscatter is recorded in both phase and amplitude. The phase is used to determine the distance from the sensor to a target, and amplitude indicates the amount of the sent signal that returns to the sensor. Amplitude measurements provide information about the roughness, geometry, wetness, and dielectric constant of that target, while phase measurements are used for SAR interferometry.

### Propagation of EM Waves

At the most fundamental level, SAR transmits an encoded burst, called a chirp, of electro-magnetic energy (Figure 1) and then listens for the return signal, called echoes.  The wavelength of this chirp is in the centimeter range, with X-band (~3 cm), C-band (~6 cm), and L-band (~23 cm) all in common use.

![Figure 1](../images/microwave-emr.png "The spectrum of electro-magnetic radiation. SAR is imaged using microwave wavelengths")

*Figure 1: The spectrum of electromagnetic radiation. SAR is imaged using microwave wavelengths. The microwave range extends from about 1 mm to 1 m in wavelength, with most radar applications using bands within the 3 mm to 30 cm range.*

### Polarizations

Polarization refers to the direction of travel of an electromagnetic wave. A horizontal wave is transmitted so that it oscillates in a plane parallel to the surface imaged, while a vertical wave oscillates in a plane perpendicular to the surface imaged. 

There are four different polarization combinations commonly used by SAR sensors: VV, VH, HV and HH, as listed in Table 1. The first letter indicates the polarization used to transmit the signal, and the second letter indicates the polarization of the measured return, as illustrated in Figure 2.

*Table 1: SAR Polarizations*

| Polarization Code | Transmit Signal Polarization | Return Signal Polarization |
|---|---|---|
| VV | Vertical | Vertical |
| VH | Vertical | Horizontal |
| HV | Horizontal | Vertical |
| HH | Horizontal | Horizontal |


![Figure 2](../images/polarizations_ASF.png "SAR signals are transmitted either vertically or horizontally. Likewise, the sensor can listen for both horizontally and vertically returns.")

*Figure 2: SAR signals are transmitted and received either vertically (V) or horizontally (H). This gives the potential for four different polarization combinations, (transmit listed first, receive second): VV, VH, HH, and HV. Credit: ASF*

Different SAR sensors have different polarization capabilities. Single-pol sensors send out a signal in one polarization and can only measure returns that are in that same polarization (VV or HH). Dual-pol sensors send out a signal in one polarization, but can measure returns that are in that same polarization (co-pol: VV or HH) as well as returns that are in the other polarization (cross-pol: VH or HV). Some SAR systems can transmit chirps with both a horizontal or vertical polarization and listen for both horizontal or vertical returns, giving full quad-pol capabilities (VV, VH, HV, HH).  


Polarimetry is an emerging field of SAR processing which is used in a number of applications such as measuring vegetation properties and changes of vegetation over time. Additional applications include oceanography, geology, and disaster response.

-------

## Backscatter Contributors

Many factors influence the backscatter received by the SAR sensor. The wavelength used by the SAR influences the signal's penetration, and, thus, what is being imaged. Surface roughness will modulate the backscatter returns from nothing up to a strong return, decreasing or increasing the brightness of the resulting pixel. Scattering mechanisms like volume scattering or double bounce can strongly influence the brightness of the SAR image as well, sometimes resulting in total saturation by the received signal.

### Wavelength

The wavelength of the SAR system influences the amount of ground penetration that occurs. As shown in Figure 3, X-band has the least penetration, scattering from the top of the canopy in vegetated areas. All three bands will penetrate dry sand, with stronger returns from both C-band and L-band. L-band has the most penetration overall, with returns from the ground in vegetated areas, strong returns from substances under dry alluvium, and deep penetration of ice and snow.

![Figure 3](../images/SAR_band_types.png "Effects of SAR band on penetration of surfaces.  The longer the wavelength, the deeper the penetration through most land types.")

*Figure 3: Effects of the SAR band on penetration of surfaces. The longer the wavelength, the deeper the penetration through most land types. Credit: [The SAR Handbook](https://gis1.servirglobal.net/TrainingMaterials/SAR/Chp2Content.pdf)*

### Surface Roughness 

The strength of the return, or backscatter, is partially based upon relative roughness of the surface imaged. The smoother the surface, the more reflection away from the sensor, while rough surfaces give a much stronger return towards the imaging platform. As can be seen in Figure 4, if the height of the surface's roughness is less than 1/32 of the wavelength, mostly specular reflection occurs. If the height of the surface's roughness is greater than 1/2 the wavelength used, the echoes are scattered in all directions, giving a strong return back to the sensor.

![Figure 4](../images/wavelength_vs_roughness.png "The amount of backscatter from a surface depends largely on the surface's roughness")

*Figure 4: The amount of backscatter from a surface depends largely on the surface's roughness, with smooth surfaces getting the least returns and rough surfaces getting the strongest returns. Credit: [The SAR Handbook](https://gis1.servirglobal.net/TrainingMaterials/SAR/Chp2Content.pdf)*

### Types of Scattering

![Figure 5](../images/scattering_types.png "Scattering mechanisms. Rough surfaces give bright returns due to the wide scattering.  Vegetated surfaces cause volumetric scattering, which has a darker return to the imaging platform.  Double bounce returns, found mostly in urban areas, give the brightest return, as the majority of the energy is re-directed back towards the sensor.")

*Figure 5: Scattering mechanisms. Rough surfaces give bright returns due to the wide scattering.  Vegetated surfaces cause volumetric scattering, which gives a darker return to the imaging platform.  Double bounce returns, found mostly in urban areas, give the brightest return, as the majority of the energy is re-directed back towards the sensor. Credit: [The SAR Handbook](https://gis1.servirglobal.net/TrainingMaterials/SAR/Chp2Content.pdf)*

The resolution of Sentinel-1 SAR images is roughly 10 m.  This means that a square of 10 meters on the ground is represented by a single pixel in the SAR image. The relative roughness of this patch of ground compared to the wavelength used will affect the backscatter strength (see Figure 4).  However, there are additional types of bounce mechanisms beyond specular and diffuse, as shown in Figure 5.  In vegetation, *volumetric* scattering occurs when signals bounce around inside the vegetation imaged.  The *double bounce* mechanism which occurs in urban areas and is exploited by corner reflectors, causes chirp to be reflected directly back to the sensor, causing a very strong backscatter.  Double bounce returns are so strong in some places that they cause over saturation of the sensor, resulting in visible sidelobes.  These sidelobes are evidenced by bright crosses surrounding the double bounce target.

------------------------

## SAR Scale

SAR backscatter are recorded in both return strength and phase.  Each pixel in a single-look complex SAR image represents these values as an imaginary number (I,Q).  To create the visible images we are used to looking at, the SAR image is *detected*.  This process calculates the square root of the sum of the squares of the I and Q values found in an SLC image, creating a so called intensity image.  This image is real valued, and, when calibrated, gives the absolute backscatter of the surface imaged.  Detected images can be stored using several different scales, including power, amplitude, and dB.  Note the default scale of Sentinel-1 RTC products from HyP3 is power. However, in some cases, it may be desirable to convert the actual pixel values to a different scale. Two other scales commonly used for SAR data are amplitude and dB.

### Power Scale

The values in this scale are generally very close to zero, so the dynamic range of the SAR image can be easily skewed by a few bright scatterers in the image. Power scale is appropriate for statistical analysis of the SAR dataset, but may not always be the best option for data visualization. 

When viewing a SAR image in power scale in a GIS environment, it may appear mostly or all black, and you may need to adjust the stretch to see features in the image. Often applying a stretch of 2 standard deviations, or setting the Min-Max stretch values to 0 and 0.3, will greatly improve the appearance of the image. You can adjust the stretch as desired to display your image to full advantage. Be aware that this does not change the actual pixel values.

### Amplitude Scale

Amplitude scale is the square root of the power scale values. This brightens the darker pixels and darkens the brighter pixels, narrowing the dynamic range of the image. In many cases, amplitude scale presents a pleasing grayscale display of RTC images. Amplitude scale works well for calculating log difference ratios (see [ASF Sentinel-1 RTC Product Guide](../guides/rtc_product_guide.md#change-detection-using-rtc-data)).

### dB Scale

The dB scale is calculated by multiplying 10 times the Log10 of the power scale values. This scale brightens the pixels, allowing for better differentiation among very dark pixels. When identifying water on the landscape, this is often a good scale to use; the water pixels generally remain very dark, while the terrestrial pixels are even brighter (see [Identifying Surface Water](../guides/rtc_product_guide.md#identifying-surface-water)).

This scale is not always the best choice for general visualization of SAR products, as it can give a washed-out appearance, and because it is in a log scale, it is not appropriate for all types of statistical analyses.

------------------------

## Geometric Distortions

There are a number of distortions inherent to SAR data due to the side-looking nature of the sensor, and these impacts will be more prevalent in areas with rugged terrain. The process of radiometric terrain correction addresses the geometric distortions that lead to geolocation errors in terrain features, and also normalizes the backscatter values based on the actual area contributing returns. This process generates an image that aligns well with other geospatial data and is suitable for GIS applications or time-series analysis.

The key distortions present in SAR images are foreshortening, layover and shadow (Figure 6).

![Figure 6](../images/sar_distortions.png "Distortions induced by side-looking SAR. Ground points a, b, c are ‘seen’ by radar as points a’, b’, c’ in the slant range.")

*Figure 6: Distortions induced by side-looking SAR. Ground points a, b, c are ‘seen’ by radar as points a’, b’, c’ in the slant range. Credit: Franz J. Meyer*

In the case of **foreshortening**, the backscatter from the front side of the mountain is compressed, with returns from a large area arriving back to the sensor at about the same time. This results in the front slope being displayed as a narrow, bright band.

When **layover** occurs, returns from the front slope (and potentially even some of the area before the slope starts) are received at the same time as returns from the back slope. Thus, area in the front of the slope is projected onto the back side in the slant range image. In this case, the data from the front slope cannot be extracted from the returns.

Another condition that results in missing data is radar **shadow**. In this case, the angle of the back slope is such that the sensor can not image it at all. These areas with steep back slopes offer no information to the SAR sensor.

When RTC is performed, foreshortened areas are corrected based on the DEM. Areas impacted by layover or shadow, however, do not actually have data returns to correct. In this case, the pixels in the resulting RTC image will have a value of No Data. We do not interpolate missing data; users who would like to fill holes with estimated values will need to do so as appropriate for their particular application.

## Speckle
  
In most cases, the patch of ground illuminated by the SAR transmitter will not be homogeneous. Instead it will be comprised of many different types of individual scatterers. The scatterers may interfere with each other either strengthening the return or weakening it. This creates a grainy (salt & pepper) appearance in SAR imagery. This a result of the nature of SAR and, thus, occurs in all SAR scenes.  Speckle in SAR images can be mitigated by multi-looking, which, in effect, uses averaging to smooth out the image, resulting in a more homogeneous appearance at the expense of resolution.
