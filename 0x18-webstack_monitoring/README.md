# 0x18. Web Stack Monitoring

## Monitoring

Just as the heart monitor in a hospital that is making sure that a patient's heart is beating and at the right beat, software monitoring will watch computer metrics, record them, and emit an alert if something is unusual or that could make the computer not work properly happens.

`You cannot fix or improve what you cannot measure` is a famous saying in the tech industry. In the age of the data-ism, monitoring how our software systems are doing is an important thing.

Web stack monitoring can be broken down into 2 categories:
### Application monitoring

Application monitoring is about getting data about your running software and making sure it is behaving as expected. Holberton gave me a link to a Wikipedia article which I assume has to do with applicaiton monitoring. I'll leave some notes about that below.

There are **two main sets of performance metrics:**
* User-end performance metrics:
	* Load times - the load is the volume of transactions processed by the application
		* transactions per second, requests per second, pages per second
	* Response times - time required for the application to respond to a user's actions at such a oad
* Computational resource metrics, which indicates whether there is adequate capacity to support the load, as well as possible locations of a performance bottleneck.

#### The "Application Performance Management" Conceptual Framework
![APM Conceptual Framework](https://upload.wikimedia.org/wikipedia/en/thumb/6/6a/APM_Conceptual_Framework.jpg/750px-APM_Conceptual_Framework.jpg)



### Server monitoring

Server monitoring is about getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload).

Back in the old days, an organization would have to spend a lot of overhead to manage their server infrastructure. But today, the Clouds reign (Google Cloud, Microsoft Azure, Amazon Web Service). These services provide Infrastructure-as-a-Service (IaaS) services on a pay-per-use basis, helping businesses scale their networking, storage, servers and virtualization capabilities in the most cost-effective manner.

As organizations deploy more servers into the cloud, security can become a growing concern. Each additional network endpoint or cloud-deployed application represents a potential attack vector that a malicious actor could exploit to gain access to the network. Maintaining the performance and availability of servers, along with their security posture, can also play an important role in optimizing customer experience and minimizing unplanned downtime.

Because of these concerns, organizations that depend on servers that are deployed in the cloud must implement server monitor solutions that help maintain the security of cloud servers while tracking their performance and availability. Server monitoring can have different objectives and track different key performance indicators (KPIs) based on the type of server, but the primary objective of server monitoring is always to protect the server from possible failure that would interrupt service availability.

**This is the basic default workflow for server monitoring:**

 1. Identify the most important Key Performance Indicators (KPIs)
 2. Set baseline KPI values
 3. Configure data collection and analysis
 4. Set up comprehensive and specific alerts

** Main key performance indicators for...**

**Web Servers**:
* Uptime
* Time to first byte
* complete page load time
* search query response time
* bounce rate

**Application servers**:
* resource usage
* data throughput
* latency
* service failures and restarts
* error and success rates
* overall application reliability

**Network servers**:
* Network connections status
* Network connection speed
* Number of connections on the network
* Packet loss and data transmission errors
* Latency or throughput
* Bandwidth utilization



## Some other famous monitoring tools:
| Tool | Description |
|------|-------------|
| New Relic | Requires you to add a piece of JavaScript to your website. Gives a detailed analysis of how quickly your website loads in a browser, with a detailed analysis at every level of the stack. If the website is loading too slowly or users are experiencing server-side errors (500 errors), there is a feature that allows you to trigger an alert.
|------|--------------|
| Uptime Robot | Checks that your website is responding from multiple locations in the world.
|------|-------------|
| Nagios | Open-source monitoring software that is slowly catching up to the world of the Cloud. As of now, ignore it.
|------|-------------|
| WaveFront | Wavefront is a cutting edge monitoring service that basically tracks all the things. A query language allows users to apply mathematical operations to these data points to etract values or detect anomalies from the time series data. While it takes some time to get used to the tool, it's the type of monitoring that the best companies are using. |


