# Credits

On Demand users are given an allotment of **{{ CREDITS_PER_MONTH }} credits per month** to use for processing jobs,
and each type of job costs a different number of credits, as shown in the [Credit Cost Table](#credit-cost-table).

The "Maximum Jobs Per Month" column displays the maximum number of jobs that you
would be able to run in a single month if you spent your entire monthly credit
allotment on jobs of that particular type.

## Credit Cost Table

| Job Type                                                      | credits | [HyP3 Basic](../about/hyp3_basic.md)<br>Max Jobs Per Month | [HyP3+](../about/hyp3_plus.md)<br>Job Cost |
|---------------------------------------------------------------|--------:|-----------------------------------------------------------:|--------------------------------------------|
| [**RTC**](../guides/rtc_product_guide.md)                     |         |                                                            |                                            |
| {{ table_indent() }} 30-m pixel spacing                       |       5 |                                {{ max_jobs_per_month(5) }} | {{ hyp3_plus_cost(5) }}                    |
| {{ table_indent() }} 20-m pixel spacing                       |      15 |                               {{ max_jobs_per_month(15) }} | {{ hyp3_plus_cost(15) }}                   |
| {{ table_indent() }} 10-m pixel spacing                       |      60 |                               {{ max_jobs_per_month(60) }} | {{ hyp3_plus_cost(60) }}                   |
| [**OPERA RTC-S1**](../guides/opera_rtc_product_guide.md)      |         |                                                            |                                            |
| {{ table_indent() }} Standard product (30-m pixel spacing)    |       1 |                                {{ max_jobs_per_month(1) }} | {{ hyp3_plus_cost(1) }}                    |
| [**InSAR**](../guides/insar_product_guide.md)                 |         |                                                            |                                            |
| {{ table_indent() }} 80-m pixel spacing (20x4 looks)          |      10 |                               {{ max_jobs_per_month(10) }} | {{ hyp3_plus_cost(10) }}                   |
| {{ table_indent() }} 40-m pixel spacing (10x2 looks)          |      15 |                               {{ max_jobs_per_month(15) }} | {{ hyp3_plus_cost(15) }}                   |
| [**ARIA S1 GUNW**](../guides/gunw_product_guide.md)           |         |                                                            |                                            |
| {{ table_indent() }} Standard product (90-m pixel spacing)    |      60 |                               {{ max_jobs_per_month(60) }} | {{ hyp3_plus_cost(60) }}                   |
| [**Burst InSAR**](../guides/burst_insar_product_guide.md)     |         |                                                            |                                            |
| {{ table_indent() }} 80-m pixel spacing (20x4 looks)          |         |                                                            |                                            |
| {{ table_indent(count=2) }} 1–4 pairs                         |       1 |                                {{ max_jobs_per_month(1) }} | {{ hyp3_plus_cost(1) }}                    |
| {{ table_indent(count=2) }} 5–15 pairs                        |       5 |                                {{ max_jobs_per_month(5) }} | {{ hyp3_plus_cost(5) }}                    |
| {{ table_indent() }} 40-m pixel spacing (10x2 looks)          |         |                                                            |                                            |
| {{ table_indent(count=2) }} 1–3 pairs                         |       1 |                                {{ max_jobs_per_month(1) }} | {{ hyp3_plus_cost(1) }}                    |
| {{ table_indent(count=2) }} 4–9 pairs                         |       5 |                                {{ max_jobs_per_month(5) }} |                                            |
| 5{{ table_indent(count=2) }} 10–15 pairs                      |      10 |                               {{ max_jobs_per_month(10) }} | {{ hyp3_plus_cost(10) }}                   |
| {{ table_indent() }} 20-m pixel spacing (5x1 looks)           |         |                                                            |                                            |
| {{ table_indent(count=2) }} 1 pair                            |       1 |                                {{ max_jobs_per_month(1) }} | {{ hyp3_plus_cost(1) }}                    |
| {{ table_indent(count=2) }} 2 pairs                           |       5 |                                {{ max_jobs_per_month(5) }} | {{ hyp3_plus_cost(5) }}                    |
| {{ table_indent(count=2) }} 3 pairs                           |      10 |                               {{ max_jobs_per_month(10) }} | {{ hyp3_plus_cost(10) }}                   |
| {{ table_indent(count=2) }} 4 pairs                           |      15 |                               {{ max_jobs_per_month(15) }} | {{ hyp3_plus_cost(15) }}                   |
| {{ table_indent(count=2) }} 5 pairs                           |      20 |                               {{ max_jobs_per_month(20) }} | {{ hyp3_plus_cost(20) }}                   |
| {{ table_indent(count=2) }} 6 pairs                           |      25 |                               {{ max_jobs_per_month(25) }} | {{ hyp3_plus_cost(25) }}                   |
| {{ table_indent(count=2) }} 7 pairs                           |      30 |                               {{ max_jobs_per_month(30) }} | {{ hyp3_plus_cost(30) }}                   |
| {{ table_indent(count=2) }} 8 pairs                           |      35 |                               {{ max_jobs_per_month(35) }} | {{ hyp3_plus_cost(35) }}                   |
| {{ table_indent(count=2) }} 9 pairs                           |      40 |                               {{ max_jobs_per_month(40) }} | {{ hyp3_plus_cost(40) }}                   |
| {{ table_indent(count=2) }} 10 pairs                          |      45 |                               {{ max_jobs_per_month(45) }} | {{ hyp3_plus_cost(45) }}                   |
| {{ table_indent(count=2) }} 11 pairs                          |      90 |                               {{ max_jobs_per_month(90) }} | {{ hyp3_plus_cost(90) }}                   |
| {{ table_indent(count=2) }} 12 pairs                          |      95 |                               {{ max_jobs_per_month(95) }} | {{ hyp3_plus_cost(95) }}                   |
| {{ table_indent(count=2) }} 13 pairs                          |     100 |                              {{ max_jobs_per_month(100) }} | {{ hyp3_plus_cost(100) }}                  |
| {{ table_indent(count=2) }} 14 pairs                          |     105 |                              {{ max_jobs_per_month(105) }} | {{ hyp3_plus_cost(105) }}                  |
| {{ table_indent(count=2) }} 15 pairs                          |     110 |                              {{ max_jobs_per_month(110) }} | {{ hyp3_plus_cost(110) }}                  |
| [**AutoRIFT**](https://its-live.jpl.nasa.gov/){target=_blank} |         |                                                            |                                            |
| {{ table_indent() }} Standard product (120-m pixel spacing)   |      25 |                               {{ max_jobs_per_month(25) }} | {{ hyp3_plus_cost(25) }}                   |

## Credit Allocation

The credit cost of a given job is roughly proportional to the computational resources required to process the job,
allowing us to distribute our resources more equitably.
This supports our mission of
[making remote-sensing data accessible](https://asf.alaska.edu/about-asf/ 'asf.alaska.edu/about-asf' ){target=_blank},
with the goal of providing valuable products to the widest breadth of users possible.

If your monthly credit allotment is not sufficient for your processing needs, you can
[purchase additional processing credits](../about/hyp3_plus.md).
Please contact us if you have questions about additional processing.

## Contact Us

{% include 'contact-snippet.md' %}
