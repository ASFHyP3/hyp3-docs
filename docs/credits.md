# Credits

<!--
TODO:
* double-check all values
-->

!!! warning "Attention"
    Beginning **April 1, 2024**, HyP3's [Monthly Processing Quota](./using/quota.md)
    will be replaced by a new **credits system.**
    You will be given an allotment of **10,000 credits per month**,
    and each type of job will cost a different number of credits,
    as shown in the table below.
    Notably, you will now be able to run up to 10,000 Burst InSAR jobs per month—a 10x increase!

    If this change impacts your current workflows, or doesn't meet your needs,
    please let us know!

| Job Type                                                                      |  Cost (credits) | Maximum Jobs Per Month[^1] |
|-------------------------------------------------------------------------------|----------------:|---------------------------:|
| [**InSAR**](/guides/insar_product_guide/)                                     |                 |                            |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 160m pixel size (20x4 looks) |              10 |                      1,000 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 80m pixel size (10x2 looks)  |              15 |                        666 |
| [**RTC**](/guides/rtc_product_guide/)                                         |                 |                            |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 30m pixel size               |               5 |                      2,000 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 20m pixel size               |              15 |                        666 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 10m pixel size               |              60 |                        166 |
| [**AutoRIFT**](https://its-live.jpl.nasa.gov/){target=_blank}                 |              25 |                        400 |
| [**Burst InSAR**](/guides/burst_insar_product_guide/)                         |               1 |                     10,000 |

In general, the credit cost of a given job is roughly proportional to the computing resources required to process the job.
Transitioning to a credits system will allow us to distribute HyP3's resources more equitably amongst our users.
This change supports our mission of [making remote-sensing data accessible](https://asf.alaska.edu/about-asf/),
with the goal of providing valuable products to the widest breadth of users possible.

If your monthly credit allotment doesn't meet your needs,
please contact us and let us know how you would like to use our service.
We have several options available for increased processing via HyP3.
All requests will be balanced against our mission: to make remote-sensing data accessible to the community.

## Contact Us

{% include 'contact-snippet.md' %}

[^1]: This is the maximum number of jobs that you would be able to run in a single month if you spent your entire monthly credit allotment on jobs of the given type. For example, if you spent all 10,000 credits on Burst InSAR jobs, then you would be able to run 10,000 jobs for that month, whereas if you spent all 10,000 credits on 10m RTC jobs, then you would only be able to run 166 jobs for that month.
