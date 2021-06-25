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

## Getting started

### Using Vertex

[Vertex](https://search.asf.alaska.edu/){target=_blank}, ASF's data search portal, is the easiest way to use HyP3.
Vertex provides a friendly interface to request jobs and review previous jobs. Visit
[On Demand Processing in Vertex](https://search.asf.alaska.edu/#/?topic=onDemand){target=_blank} to learn more.

### Using the Python SDK

The HyP3 SDK is a Python library for using HyP3 programmatically. It is available on both
[conda-forge](https://anaconda.org/conda-forge/hyp3_sdk){target=_blank} and
[PyPI](https://pypi.org/project/hyp3-sdk/){target=_blank}, and can be installed with either:
```
conda install -c conda-forge hyp3_sdk
```

or
```
python -m pip install hyp3_sdk
```

Visit [Using HyP3: SDK](using/sdk.md) to learn more.

### Using the API

The HyP3 web API is the backbone behind Vertex and the SDK. You may also use the API directly. Visit
[Using HyP3: API](using/api.md) to learn more.

## News and Notes

Follow us on Twitter, or check our [News and Notes](news.md) page, to keep up to date on all things HyP3!

<a class="twitter-timeline" data-height="400" href="https://twitter.com/ASFHyP3">Tweets by ASFHyP3</a>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## Contact Us

{% include 'contact-snippet.md' %}
