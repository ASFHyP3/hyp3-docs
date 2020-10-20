# ASF HyP3

***Alaska Satellite Facility's Hybrid Pluggable Processing Pipeline***

HyP3 is a service for processing Synthetic Aperture Radar (SAR) imagery that addresses many common issues for users of
SAR data:

* Most SAR datasets require at least some processing to remove distortions before they are analysis-ready
* SAR processing is computing-intensive
* Software for SAR processing is complicated to use and/or prohibitively expensive
* Producing analysis-ready SAR data has a steep learning curve that acts as a barrier to entry

HyP3 solves these problems by providing a free service where people can request SAR processing on-demand. These
processing requests are picked up by automated systems, which handle the complexity of SAR processing on behalf of the
user. HyP3 doesn't require users to have a lot of knowledge of SAR processing before getting started; users only need to
submit the input data and set a few optional parameters if desired. With HyP3, analysis-ready products are just a few
clicks away.

## How it Works

HyP3 is built around three core concepts: Platform, Plugins, and Products.

The HyP3 platform makes it easy for users to request processing, monitor their requests, and download processed
products. The platform delegates each processing request to a plugin on the user's behalf. A deployment of the HyP3
platform can be integrated with any number of plugins.

Plugins are the workhorses of HyP3. Each plugin implements a particular SAR processing workflow.  When invoked, they
marshal input data and generate an output product. Plugins are container-based and can be used independently of the
platform.

Products are the end result of processing, typically one or more data files.

## Contact Us

Want to talk about HyP3? We would love to hear from you!

Found a bug? Want to request a feature?
[open an issue](https://github.com/ASFHyP3/ASFHyP3/issues/new)

General questions? Suggestions? Or just want to talk to the team?
[chat with us on gitter](https://gitter.im/ASFHyP3/community)
