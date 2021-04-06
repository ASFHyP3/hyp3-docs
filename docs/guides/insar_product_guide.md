# Sentinel-1 InSAR Product Guide
##Introduction
Interferometric SAR (InSAR) processing uses two SAR images of the same area to determine geometric properties of the surface. With InSAR, Digital elevation models (DEMs) can be routinely created (SRTM, GLO-30). Moreover, two or more pairs of images can be used to extract surface motion or deformation at the millimeter level scale.

###Brief Overview of InSAR
SAR is an active sensor that transmits pulses and listens for echoes. These echoes are recorded in phase and amplitude, with the phase being used to determine the distance from the sensor to the target and the amplitude yeilding information about the roughness and dielectric constant of that target.

InSAR expliots the phase difference between two SAR images, creating an interferogram that shows where the phase, and therefore the distance to the target, has changed from one pass to the next.  There are several factors that influence the interferogram including earth curvature, topographic effects, atmospheric delays, and surface motion.  With the proper processing, InSAR can be used to create topographic maps and to detect millimeter scale changes in the earth's surface. Applications include volcanic deformation, susidence, landslide detection, and earthquake assessment.

###Contents of InSAR guide
This product guide includes relevant background information on radar and, more specifically, SAR imagery. The InSAR workflow used to create HyP3 InSAR surface motion products constitute a large portion of this document.  Users are cautioned to read the sections on limitations and error sources in InSAR products.  Finally, data sources and application examples are presented.

##Background
###Propagation of EM Waves
####Types of scattering
####Polarizations
###Synthetic Aperture Radar
####Geometric Distortions
####Speckle
####Geocoding
####Acquisition modes
####Product Levels
##InSAR Workflow
###Image co-registration
###Common-band filtering
###Baseline calculation
###Interferogram creation
###Ellipsoidal fringe removal (phase flattening)
###Coherence Estimation
###Interferogram filtering
###Phase unwrapping
###Computation of heights
###Resampling to map coordinates
##Differential InSAR
###Removal of topographic phase
###Removal of differential phase
##Limitations
##Error Sources
##Data Sources
##Examples
###Surface Deformation 
###Volcanic Deformation
###Subsidence
###Earthquakes
##Data Access

