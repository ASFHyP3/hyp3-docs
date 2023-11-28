# Using the HyP3 SDK to process new granules for given search parameters

In the past, ASF offered subscription functionality for HyP3 products.
A user could create a subscription with a particular set of search parameters
(date range, area of interest, etc.),
and new Sentinel-1 acquisitions that met these criteria would be automatically submitted for processing.
However, this feature was only accessed by a very small minority of HyP3 users,
and most users did not regularly check their subscriptions and download the generated products before they expired.
As such, we have removed this feature in favor of a more flexible approach.

The following Jupyter notebooks demonstrate how to achieve subscription-like functionality.
They can be run as needed so that you do not have to worry about your products expiring
before you are ready to download them.
This workflow is particularly useful for ongoing monitoring of a geographic area of interest.

The first notebook demonstrates how to submit RTC jobs using this method,
while the second notebook demonstrates how to submit InSAR jobs.
These tutorials can easily be adapted to support other job types.
Please [contact us](../contact.md) if you need help adapting these tutorials for your particular use case.

* [Using the HyP3 SDK to generate RTC products for given search parameters](https://nbviewer.org/github/ASFHyP3/hyp3-docs/blob/main/docs/tutorials/new-rtc-jobs.ipynb "Using the HyP3 SDK to generate RTC products for given search parameters" ){target=_blank}
* [Using the HyP3 SDK to generate InSAR products for given search parameters](https://nbviewer.org/github/ASFHyP3/hyp3-docs/blob/main/docs/tutorials/new-insar-jobs.ipynb "Using the HyP3 SDK to generate InSAR products for given search parameters" ){target=_blank}
