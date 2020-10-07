# ASFHyP3
A collection of services and plugins to support HyP3 by the Alaska Sattelite Facility.

# What is HyP3
HyP3 (Hybrid Pluggable Proccesing System) is a System that sets forth to solve many of the issues that people face when processing SAR (synthetic apature radar) imagry:
* SAR processing requires a lot of compute resources
* Software to do SAR processing is complicated to use and/or prohibitidvely expensive
* Most SAR datasets require at least some processing to remove distortions before they are analysis ready
* Producing analysis ready SAR data has a steep learning curve that acts as a barrier to entry

HyP3 solves these problems by providing a **free** service where people can request SAR processing on-demand. These processing requests are picked up by automated systems which handle the complexity of SAR processing on the users behalf. HyP3 doesn't require users hava a lot of knowledge of SAR processing before getting started, intstead, users only need to submit the input data, and a few optional parameters if desired. With HyP3, analysis ready products as as easy as a few clicks.

# How it Works
HyP3 is made up of multiple parts, but they fall into roughly 2 categories Orchestration and Plugins. 

Plugins are the workhorses of HyP3, they marshal the input data of a process through the complicated SAR processing code to seemlessly get an output product. Plugins are container based and can be used independantly. 

The Orchestration of HyP3 runs HyP3 plugins in the cloud and makes it easy for users to request processing, monitor their requests, and download finished products without needing to manage any of the plugins. Hyp3 Orchestration can also be deployed independantly.

# Contributing

# Contact Us
Want to talk about HyP3, We would love to hear from you!

Found a bug? Want to request a feature? [open an issue](https://github.com/ASFHyP3/ASFHyP3/issues/new) 

General questions? Suggstions? Or just want to talk to the team? [chat with us on gitter](https://gitter.im/ASFHyP3/community)
