[//]: # (Image References)

[monitoring_installation]: ./answer-img/01-monitoring_installation.PNG
[kubectl_get_all]: ./answer-img/kubectl_get_all.PNG
[pods_svc_monitoring]: ./answer-img/kubectl_get_pods_svc_monitoring.PNG
[pods_svc_observability]: ./answer-img/kubectl_get_pods_svc_observability.PNG

[login]: ./answer-img/02-Grafana_login.PNG
[1_dashboard]: ./answer-img/03-Basic_dashboard.PNG
[2_dashboard]: ./answer-img/03b-Basic_dashboard.PNG

[40X_50X_SLI]: ./answer-img/40X_50X_SLI.PNG

[flask_backend]: ./answer-img/tracing_flask_backend_app.PNG
[Jaeger_Dashboards]: ./answer-img/Jaeger_Dashboards.PNG

[final_dashboard]: ./answer-img/final_dashboard.PNG

**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation
![][monitoring_installation]

### Namespace: Default
![][kubectl_get_all] 
### Namespace: Monitoring
![][pods_svc_monitoring]
### Namespace: Observability
![][pods_svc_observability] 

## Setup the Jaeger and Prometheus source
* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
![][login] 

## Create a Basic Dashboard
* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
![][1_dashboard]
![][2_dashboard]

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
* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

![][40X_50X_SLI]

## Tracing our Flask App
* We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.

["./reference-app/backend/app.py"] is the python file for trace code.

* prerequisite
- kubectl port-forward service/backend-service 8081:8081
- kubectl port-forward -n observability service/my-traces-query --address 0.0.0.0 16686:16686

* Generate traffic request for api endpoint
 
for i in 1 2 3; do curl localhost:8081; done
for i in 1 2 3 4 5 6 7 8 9; do curl localhost:8081/api; done

for i in 1 2 3 4 5 6 7 8 9; do curl localhost:8081/star; done
for i in 1 2 3; do curl localhost:8081/error_410; done
for i in 1 2 3; do curl localhost:8081/error_500; done
for i in 1 2 3; do curl localhost:8081/healthz; done

![][flask_backend]

## Jaeger in Dashboards
* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

![][Jaeger_Dashboards]

## Report Error
* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name: Error on "./reference-app/backend/app.py" 

Date: 04 Nov 2021, 09:29:23

Subject: "/star" request end point failure

Affected Area: "./reference-app/backend/app.py" line no 98

Severity: Critical

Description: When user access backend api with url end point "/star" with post request, it produce error 405 Method Not Allowed , possible because MongoDB database setting is not properly configured.

## Creating SLIs and SLOs
* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

- [SLOs] application has 99.95% uptime per month, to meet this SLOs we need to design SLI 

Suggest to measure

- Percentage of CPU in last 1 month (for saturation).
- Memory consumption in last 1 month (for saturation).
- Percentage of Infrastructure uptime in the last 1 month (to check error).
- Average number of requests per minute in the last 24 hours (to check traffic).
- % of request/response time less than 250 milliseconds (for latency).

Prepare errors budget as all the applications may not always work perfectly.
- Applications to produce 5xx status code less than 1% in next month.
- Service downtime to be 0.01% in next month.

## Building KPIs for our plan
Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

To achieve our SLO, would collect KPIs everyday

### KPI for saturation
How "full" your service is. A measure of system fraction, emphasizing the resources that are most constrained (e.g., in a memory-constrained system, show memory; in an I/O-constrained system, show I/O) as many systems degrade in performance before they achieve 100% utilization, so having a utilization target is essential.

* CPU consumption should be less than 85%
* Memory consumption should be less than 85%

### KPI for Uptime
Uptime need to be approximate 99 percent within a month and response time should be around 500 milliseconds.

* application uptime should be greater than 99.5%
* % of request under 250ms should be more than 99%

### KPI for Errors
The rate of requests that fail, either explicitly (e.g., HTTP 500s), implicitly (for example, an HTTP 200 success response, but coupled with wrong message) to be measured.

* errors per second (non HTTP 200) in last 3 hour
* successful request (HTTP 200) per second in last 3 hour

### KPI for Traffic
A measure of how much demand is being placed on your system, measured in a high-level system-specific metric.
* Average response response time measured over 30 seconds intervals for successful requests in last 3 hour.


## Final Dashboard
* Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

![][final_dashboard]

* CPU Usages: The CPU usage of the Flask backend app as measured over 30 seconds.
* Memory usages: The memory usage of the Flask backend app.
* Uptime: Uptime of each pod.
* 40X HTTP: 40X HTTP error code.
* 50X HTTP: 50X HTTP error code.
* Errors_per_second: Number of failed (non HTTP 200) responses per second.
* successful_requests_per_sec : Number of successful Flask requests per second.
* average_response_time [30s]: The average response time measured over 30 seconds intervals for successful requests
* Requests_under_250ms: The percentage of successful requests finished within 1/4 second.