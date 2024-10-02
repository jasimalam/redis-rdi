
## How RDI Work

RDI synchronizes the dataset between the source and target using a data pipeline that implements several processing steps in sequence:

1. A CDC collector captures changes to the source database. RDI currently uses an open source collector called [Debezium](https://debezium.io/) for this step.
2. The collector records the captured changes using Redis streams in the RDI database.
3. A stream processor reads data from the streams and applies any transformations that you have defined (if you don't need any custom transformations then it uses defaults). It then writes the data to the target database for your app to use.



## How RDI is deployed

RDI is designed with two planes that provide its services. 

The **control plane** contains the processes that keep RDI active. It includes:

- An operator process that schedules the CDC collector and the stream processor to implement the two phases of the pipeline lifecycle (initial cache loading and change streaming)
- A Prometheus endpoint to supply metrics about RDI
- A REST API to control the VM.

The **management plane** provides tools that let you interact with the control plane. Use the CLI tool to install and administer RDI and to deploy and manage a pipeline. Use the pipeline editor (included in Redis Insight) to design or edit a pipeline. The diagram below shows the components of the control and management planes and the connections between them:

![RDI Deployment](/docs/images/ingest-control-plane.png)

## RDI on your own VMs
For this deployment, you must provide two VMs. The collector and stream processor are active on one VM while the other is a standby to provide high availability. The operators run on both VMs and use an algorithm to decide which is the active one (the "leader"). Both the active VM and the standby need access to the authentication secrets that RDI uses to encrypt network traffic. The diagram below shows this configuration:

![RDI VM HA](/docs/images/ingest-active-passive-vms.png)

