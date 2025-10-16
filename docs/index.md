# **Hybrid Pluggable Processing Pipeline (HyP3)**

The Alaska Satellite Facility's HyP3 (pronounced *"hype"*) platform supports processing Synthetic Aperture Radar (SAR) 
imagery in a cloud-native computing environment. It addresses many common issues for users of SAR data:

* Most SAR datasets require at least some processing to remove distortions before they are analysis-ready
* SAR processing is computing-intensive
* Software for SAR processing is complicated to use and/or prohibitively expensive
* Producing analysis-ready SAR data has a steep learning curve that acts as a barrier to entry

HyP3 solves these problems by providing a service where people can request SAR processing on demand. These
processing requests are picked up by automated systems, which handle the complexity of SAR processing on behalf of the
user. 

HyP3 doesn't require users to have a lot of knowledge of SAR processing before getting started; users only need to
submit the input data and set a few optional parameters if desired. With HyP3, analysis-ready products are just a few
clicks away.

<table class="tg"><thead>
  <tr>
    <th class="tg-fymr">
        <a href="/about/hyp3_basic/" title="HyP3 Basic"><b>HyP3 Basic</b></a><br><em>Supported by NASA Earthdata</em>
    </th>
    <th class="tg-fymr">
        <a href="/about/hyp3_plus/" title="HyP3+"><b>HyP3+</b></a> 
    </th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0pky">
      <a href="https://hyp3-api.asf.alaska.edu" title="HyP3 API" target="_blank">hyp3-api.asf.alaska.edu</a><br><br>Products expire after 14 days<br><br>Round-robin processing queue<br><br><br>Products distributed via CloudFront
    </td>
    <td class="tg-0pky">
      <a href="https://hyp3-plus.asf.alaska.edu" title="HyP3 Plus API" target="_blank">hyp3-plus.asf.alaska.edu</a><br><br>Products expire after 30 days<br><br>Smaller user-queue with higher throughput.<br>Get your products faster!<br><br>Products provided in a public AWS S3 Bucket<br>
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">10,000 Credits/ month free*</td>
    <td class="tg-0pky">1 Credit = $0.05</td>
  </tr>
</tbody></table>

## Getting started

{% include 'using-snippet.md' %}

## What's New

Follow [@ASFHyP3](https://twitter.com/ASFHyP3 "https://twitter.com/ASFHyP3" ){target=_blank} on Twitter, or check our 
[What's New](whats_new.md "HyP3 What's New" ){target=_blank} page to keep up to date on all things HyP3!

## Contact Us

{% include 'contact-snippet.md' %}
