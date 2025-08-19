# Using the HyP3 SDK to process new granules for given search parameters

In the past, ASF offered subscription functionality for HyP3 products.
A user could create a subscription with a particular set of search parameters (date range, area of interest, etc.), 
and new Sentinel-1 acquisitions that met these criteria would be automatically submitted for processing.

The following Jupyter notebooks demonstrate how to achieve subscription-like functionality. 
This workflow is particularly useful for ongoing monitoring of a geographic area of interest.

The first notebook demonstrates how to submit RTC jobs using this method, while the second notebook demonstrates 
how to submit InSAR jobs. These tutorials can easily be adapted to support other job types. 
Please [contact us](../contact.md) if you need help adapting these tutorials for your particular use case.

* [Using the HyP3 SDK to generate RTC products for given search parameters](https://github.com/ASFHyP3/hyp3-docs/blob/main/docs/tutorials/new-rtc-jobs.ipynb "Using the HyP3 SDK to generate RTC products for given search parameters" ){target=_blank}
* [Using the HyP3 SDK to generate InSAR products for given search parameters](https://github.com/ASFHyP3/hyp3-docs/blob/main/docs/tutorials/new-insar-jobs.ipynb "Using the HyP3 SDK to generate InSAR products for given search parameters" ){target=_blank}
