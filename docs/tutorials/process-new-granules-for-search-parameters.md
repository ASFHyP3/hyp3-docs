# Using HyP3 to Process New Granules for Given Search Parameters

In the past, ASF offered subscription functionality for HyP3 products.
A user could create a subscription with a particular set of search parameters
(date range, area of interest, etc.),
and new Sentinel-1 acquisitions that met these criteria would be automatically submitted for processing.
However, this feature was only accessed by a very small minority of HyP3 users,
and most users did not regularly check their subscriptions and download the generated products before they expired.
<!-- TODO: change "deprecated" to "removed" per https://asfdaac.atlassian.net/browse/TOOL-2086 -->
As such, we have deprecated this feature in favor of a more flexible approach.

The following Jupyter notebooks demonstrate how to achieve subscription-like functionality.
They can be run as needed, so that you do not have to worry about your products expiring
before you are ready to download them.
This workflow is particularly useful for ongoing monitoring of a geographic area of interest.

The first notebook demonstrates how to submit RTC jobs using this method,
while the second notebook demonstrates how to submit InSAR jobs.
These tutorials can easily be adapted to support other job types.
Please [contact us](../contact.md) if you need help adapting these tutorials for your particular use case.

TODO: link to the notebooks
