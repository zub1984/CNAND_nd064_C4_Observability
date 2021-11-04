[//]: # (Image References)

[image1]: ./answer-img/01-monitoring_installation.PNG
[image2]: ./answer-img/02-Grafana_login.PNG
[image3]: ./answer-img/03-Basic_dashboard.PNG

**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation
![][image1] 

## Setup the Jaeger and Prometheus source
* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
![][image2] 

## Create a Basic Dashboard
* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
![][image3]

## Describe SLO/SLI
* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

- SLO : A Service-Level Objective (SLO) is a measurable goal set by the SRE (Site Reliability Engineering) team to ensure a standard level of performance during a specified period of time. 

- SLI : A Service-Level Indicator (SLI) is a specific metric used to measure the performance of a service. Sometimes the term SLI is used to refer to the general metric—such as uptime but really what we need in the end is an actual measurement.

For example, suppose that team has following SLO:

<I>The application will have an uptime of 99.9% during the next year.</I>

In this case, SLI would be the actual measurement of the uptime. Perhaps during that year, you actually achieved 99.5% uptime or 97.3% uptime. These measurements are your SLIs—they indicate the level of performance your service actually exhibited, and show you whether you achieved your SLO (in this case, the SLIs show that performance fell short of the objective).

## Creating SLI metrics.
* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

Without a measurement, it’s impossible to know what you’re doing well and what needs improvement. When you introduce customer service metrics into the mix, you suddenly have concrete, objective data to inform your decisions. What could be better? Business owners who don’t measure customer service are taking a stab in the dark when they try to improve: They don’t know what’s wrong, so they’re just guessing.

Example : Suppose you are monitoring the performance of services at a fast food restaurant. Here are some reasonable examples that might be interested

* Number of orders completed/hour.
* Number of 5-star ratings/day.
* Number of cancelled orders/week.
* Piza sold/month.
* % of late orders (fulfillment time > 10 minutes)/hour.

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

- [Latency]: % of late response (Response time > 5ms)/hours
- [Failure rate]: Number of failure code (40X and 50X)/day
- [Uptime]: Uptime nedd to be approximate 99 percent within a month and response time should be around 500 milliseconds.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
