# Sentinel-1 InSAR Product Guide

## Introduction
Interferometric SAR (InSAR) processing uses two SAR images of the same area to determine geometric properties of the surface. With InSAR, Digital elevation models (DEMs) can be routinely created (SRTM, GLO-30). Moreover, two or more pairs of images can be used to extract surface motion or deformation at the millimeter level scale.

### Brief Overview of InSAR
SAR is an active sensor that transmits pulses and listens for echoes. These echoes are recorded in phase and amplitude, with the phase being used to determine the distance from the sensor to the target and the amplitude yeilding information about the roughness and dielectric constant of that target.

![Figure 1](../images/phase_diff.png "Difference in range shows movement of the surface imaged")

*Figure 1: Two passes of an imaging SAR taken at time T<sub>0</sub> and T<sub>0</sub> + ∆t, will give two distances to the ground, R<sub>1</sub> and R<sub>2</sub>.  A difference between R<sub>1</sub> and R<sub>2</sub> shows motion on the ground.  In this case, a subsidence makes R<sub>2</sub> greater than R<sub>1</sub>. Credit: Franz J Meyer*

InSAR expliots the phase difference between two SAR images to create an interferogram that shows where the phase, and therefore the distance to the target, has changed from one pass to the next as illustrated in figure 1.  There are several factors that influence the interferogram including earth curvature, topographic effects, atmospheric delays, and surface motion.  With the proper processing, InSAR can be used to create topographic maps and to detect millimeter scale changes in the earth's surface. Applications include volcanic deformation, susidence, landslide detection, and earthquake assessment.

### Contents of InSAR guide
This product guide includes relevant background information on radar and, more specifically, SAR imagery. The InSAR workflow used to create HyP3 InSAR surface motion products constitute a large portion of this document.  Users are cautioned to read the sections on limitations and error sources in InSAR products.  Finally, data sources and application examples are presented.

## Background
### Propagation of EM Waves

![Figure 2](../images/microwave-emr.png "The spectrum of electro-magnetic radiation. SAR is imaged using microwave wavelengths (&#955 ≈ 3-23 cm)")
 
*Figure 2: The spectrum of electro-magnetic radiation. SAR is imaged using microwave wavelengths (&#955 ≈ 3-23 cm)*

![Figure 3](../images/SAR_band_types.png "Effects of SAR band on penetration of surfaces.  The longer the wavelength, the deeper the penetration through most land types.")

*Figure 3: Effects of the SAR band on penetration of surfaces.  The longer the wavelength, the deeper the pentration through most land types.*


At the most fundamental level, SAR transmits an encoded burst, called a chirp, of electro-magnetic energy (figure 2) and then listens for the return signal, called echoes.  The wavelength of this chirp is in the centimeter range, with X-band (~3 cm), C-band (~6 cm), and L-band (~23 cm) all in common use. As shown in figure 3, X-band has the least penetration, scattering from the top of the canopy in vegetated areas.  All three bands will penetrate dry sand, with stronger returns from both C-band and L-band.  L-band has to most penetration overall, with returns from the ground in vegetated areas, stong returns from substances under dry alluvium, and deep penetration of ice and snow.

The strength of the return is based upon relative roughness of the surface imaged. The smoother the surface, the more reflection away from the sensor, with rough surfaces give a much stronger return towards the imaging platform. As can be seen in figure 4, if the height of the surface's roughness is less than 1/32 of the wavelength, mostly specular reflection occurs. If the height of the surface's roughness is grater than 1/2 the wavelength used, the echoes are scattered in all directions, giving a strong return back to the sensor.

![Figure 4](../images/wavelength_vs_roughness.png "The amount of backscatter from a surface depends largely on the surface's roughness")

*Figure 4: The amount of backscatter from a surface depends largely on the surface's roughness, with smooth surfaces getting the least returns and rough surfaces getting the strongest returns.*

#### Types of scattering

![Figure 5](../images/scattering_types.png "Scattering mechanisms.  Rough surfaces give bright returns, vegetated surfaces have relatively less returns to the imaging platform.  Double bounce returns, found mostly in urban areas, give the brightest return, as all of the energy is re-directed back towards the sensor.")

*Figure 4: Scattering mechanisms.  Rough surfaces give bright returns, vegetated surfaces have relatively less returns to the imaging platform.  Double bounce returns, found mostly in urban areas, give the brightest return as all of the energy is re-directed back towards the sensor.*

#### Polarizations
### Synthetic Aperture Radar
#### Geometric Distortions
#### Speckle
#### Geocoding
#### Acquisition modes
#### Product Levels
## InSAR Workflow
### Image co-registration
### Common-band filtering
### Baseline calculation
### Interferogram creation
### Ellipsoidal fringe removal (phase flattening)
### Coherence Estimation
### Interferogram filtering
### Phase unwrapping
### Computation of heights
### Resampling to map coordinates
## Differential InSAR
### Removal of topographic phase
### Removal of differential phase
## Limitations
## Error Sources
## Data Sources
## Examples
### Surface Deformation 
### Volcanic Deformation
### Subsidence
### Earthquakes
## Data Access

