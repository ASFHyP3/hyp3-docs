# Credits

!!! warning "Attention"
    On **April 1st 2024**, ASF's On Demand Monthly Processing Quota (1000 jobs per 
    month) was replaced by a new **credit system**.
    You are now given an allotment of **10,000 credits per month**,
    and each type of job costs a [different number of credits to process](#credit-cost-table). 
    Notably, you can now run up to 10,000 Burst InSAR jobs per month — 
    a 10x increase!

    This change affects all ASF On Demand users,
    whether you are accessing our service via [Vertex](/using/vertex){target=_blank},
    the [HyP3 SDK](/using/sdk){target=_blank}, or the [HyP3 API](/using/api){target=_blank}.

    If this change adversely impacts your current workflows, or doesn't meet your needs,
    please [let us know!](/contact)

On Demand users are given an allotment of **10,000 credits per month** to use for 
processing jobs, and each type of job costs a different number of credits, as shown in the [Credit Cost Table](#credit-cost-table).

The "Maximum Jobs Per Month" column displays the maximum number of jobs that you 
would be able to run in a single month if you spent your entire monthly credit 
allotment on jobs of that particular type.

## Credit Cost Table
| Job Type                                                                         |  Cost (credits) | Maximum Jobs Per Month |
|----------------------------------------------------------------------------------|----------------:|-----------------------:|
| [**InSAR**](/guides/insar_product_guide/)                                        |                 |                        |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 80-m pixel spacing (20x4 looks) |              10 |                  1,000 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 40-m pixel spacing (10x2 looks) |              15 |                    666 |
| [**RTC**](/guides/rtc_product_guide/)                                            |                 |                        |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 30-m pixel spacing              |               5 |                  2,000 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 20-m pixel spacing              |              15 |                    666 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 10-m pixel spacing              |              60 |                    166 |
| [**AutoRIFT**](https://its-live.jpl.nasa.gov/){target=_blank}                    |              25 |                    400 |
| [**Burst InSAR**](/guides/burst_insar_product_guide/)                            |               1 |                 10,000 |

The credit cost of a given job is roughly proportional to the computational resources required to process the job.
Transitioning to a credits system allows us to distribute our resources more equitably.
This change supports our mission of [making remote-sensing data accessible](https://asf.alaska.edu/about-asf/ 'asf.alaska.edu/about-asf' ){target=_blank},
with the goal of providing valuable products to the widest breadth of users possible.

If your monthly credit allotment doesn't meet your needs,
please contact us and let us know how you would like to use our service.
We may be able to support increased processing, depending on your requirements.
All requests will be balanced against our mission: to make remote-sensing data accessible to the community.

## Contact Us

{% include 'contact-snippet.md' %}
