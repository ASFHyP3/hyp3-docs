# On Demand Sentinel-1 Processing in Vertex

The Alaska Satellite Facility offers 
[On Demand processing of Sentinel-1 datasets to Radiometric Terrain Correction (RTC) or Interferometric SAR (InSAR) products through Vertex](https://search.asf.alaska.edu/#/?topic=onDemand "Vertex On Demand Documentation" ){target=_blank}, 
ASF's Data Search web portal. You can submit scenes to be processed into higher-level products, avoiding the 
cost and complexity of performing such processing yourself.

[![Vertex Image](../images/vertex.png "Click to open Vertex in a new tab")](https://search.asf.alaska.edu/ "https://search.asf.alaska.edu" ){target=_blank}

On Demand products are generated using ASF's 
[HyP3 processing platform](../index.md "Jump to the HyP3 landing page of this documentation"). Refer to the 
[Products](../products.md "Jump to the Products page of the documentation") page for more information about the 
various On Demand products ASF offers. 

## Getting Started

To request On Demand products, visit 
[ASF Data Search - Vertex](https://search.asf.alaska.edu "https://search.asf.alaska.edu" ){target=_blank} 
and [Sign In with your Earthdata Login credentials](authentication.md#authentication-in-vertex).

1. **Select your scenes** - RTC processing is available for Sentinel-1 GRD-H and SLC scenes with a beam mode of IW. 
   InSAR processing requires pairs of IW SLC scenes or bursts. Use the Geographic Search in Vertex to find individual 
   scenes to submit for RTC processing, or to find reference scenes to use for generating InSAR pairs. For InSAR, once 
   you find a reference scene or burst, use either the 
   [Baseline](https://docs.asf.alaska.edu/vertex/baseline/ "Vertex Baseline Documentation" ){target=_blank} 
   or [SBAS](https://docs.asf.alaska.edu/vertex/sbas/ "Vertex SBAS Documentation" ){target=_blank} 
   Search to find scene pairs to submit for processing. 

2. **Submit your request** - After selecting your scenes, access the  *On Demand* 
   <img width="30" src="https://user-images.githubusercontent.com/17994518/95892024-588b9280-0d32-11eb-8734-f1a54a9d2a20.png" /> 
   queue to submit your processing request. You may process jobs worth up to a total of {{ CREDITS_PER_MONTH }} 
   credits per month. See our [Credits](./credits.md) page for more details.

3. **Monitor your request** - The *On Demand Products* search type displays your running and completed requests. 
   New requests are typically available for download within an hour, but wait time will depend on processing load.

4. **Download your data** - Finished On Demand products can be downloaded after an *On Demand Products* search either 
   directly <img width="25" src="https://user-images.githubusercontent.com/17994518/95271858-6ea5ca00-07eb-11eb-9217-a280ca57a5e6.png" /> 
   or via your download queue 
   <img width="25" src="https://user-images.githubusercontent.com/17994518/95271856-6d749d00-07eb-11eb-81d8-365a6221e4f1.png" />. 
   On Demand products are retained and available to download for two weeks after processing.

## Tutorials

Refer to our 
[StoryMap Tutorials](https://asf-daac.maps.arcgis.com/home/index.html "https://asf-daac.maps.arcgis.com/home/index.html" ){target=_blank} 
for step-by-step guidance on submitting, downloading, and working with many of the different On Demand products 
available from ASF.

[![StoryMap Tutorials](../images/story-map-tutorials.png "Click to open ASF AGOL Homepage")](https://asf-daac.maps.arcgis.com/home/index.html "https://asf-daac.maps.arcgis.com/home/index.html" ){target=_blank}