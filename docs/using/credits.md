# Credits

<!--
TODO:
* double-check all values
-->

!!! warning "Attention"
    Beginning **April 1st**, ASF's On Demand [Monthly Processing Quota](/using/quota)
    will be replaced by a new **credits system**.
    You will be given an allotment of **10,000 credits per month**,
    and each type of job will cost a different number of credits,
    as shown in the table below.
    Notably, you will now be able to run up to 10,000 Burst InSAR jobs per month—a 10x increase!

    This change will affect all ASF On Demand users,
    whether you are accessing our service via [Vertex](/using/vertex),
    the [HyP3 SDK](/using/sdk), or the [HyP3 API](/using/api).

    If this change adversely impacts your current workflows, or doesn't meet your needs,
    please [let us know!](/contact)

The table below displays the credit cost for each type of job.
The "Maximum Jobs Per Month" column displays the maximum number of jobs that you would be able to run
in a single month if you spent your entire monthly credit allotment on jobs of the given type.

| Job Type                                                                      |  Cost (credits) | Maximum Jobs Per Month |
|-------------------------------------------------------------------------------|----------------:|-----------------------:|
| [**InSAR**](/guides/insar_product_guide/)                                     |                 |                        |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 160m pixel size (20x4 looks) |              10 |                  1,000 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 80m pixel size (10x2 looks)  |              15 |                    666 |
| [**RTC**](/guides/rtc_product_guide/)                                         |                 |                        |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 30m pixel size               |               5 |                  2,000 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 20m pixel size               |              15 |                    666 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 10m pixel size               |              60 |                    166 |
| [**AutoRIFT**](https://its-live.jpl.nasa.gov/){target=_blank}                 |              25 |                    400 |
| [**Burst InSAR**](/guides/burst_insar_product_guide/)                         |               1 |                 10,000 |

The credit cost of a given job is roughly proportional to the computational resources required to process the job.
Transitioning to a credits system allows us to distribute our resources more equitably.
This change supports our mission of [making remote-sensing data accessible](https://asf.alaska.edu/about-asf/),
with the goal of providing valuable products to the widest breadth of users possible.

If your monthly credit allotment doesn't meet your needs,
please contact us and let us know how you would like to use our service.
We have several options available for increased processing.
All requests will be balanced against our mission: to make remote-sensing data accessible to the community.

## Contact Us

{% include 'contact-snippet.md' %}
