## Monitoring and Management

### From Command-Line

Check Current Contex:

```bash
# redis-di list-contexts
+--------------+-----------+-----------------+--------------------+----------------------+--------------+
| Context Name | Is Active | Cluster Address | Cluster Username   | RDI Database Address | RDI Username |
+--------------+-----------+-----------------+--------------------+----------------------+--------------+
| default      | True      | 10.56.8.89:9443 | jasim@example.com  | 10.56.8.89:12001     |              |
+--------------+-----------+-----------------+--------------------+----------------------+--------------+
```
Check RDI status:

```bash
# redis-di status --rdi-password '[REDACTED]'
```


### Redis Insight

Login to RDI via Redis Insight
![RDI Login via Insight](/docs/images/rdi-insight.png)

We may configure pipeline via Redis Insight
![RDI Pipleline](/docs/images/rdi-pipeline-insight.png)

RDI Status Dahhbaord Can be Monitored via Redis Insight
![RDI Dashboard](/docs/images/rdi-insight-dashboard.png)

### Prometheus

RDI out of the box expose promehteus metrics. Access Prometheus metrics:

- **Collector metrics** endpoint: https://<RDI_HOST>/metrics/collector-source
- **Stream processor** metrics endpoint:  https://<RDI_HOST>/metrics/rdi


### Logging

RDI uses fluentd and logrotate to ship and rotate logs for its Kubernetes (K8s) components. 

By default, RDI stores logs in the host VM file system at */opt/rdi/logs*.

| Filename                                   | Phase                                                               |
|--------------------------------------------|---------------------------------------------------------------------|
| rdi_collector-collector-initializer.log    | Initializing the collector.                                         |
| rdi_collector-debezium-ssl-init.log        | Establishing the connector SSL connections to the source and RDI database (if you are using SSL). |
| rdi_collector-collector-source.log         | Collector change data capture (CDC) operations.                     |
| rdi_rdi-rdi-operator.log                   | Main RDI control plane component.                                   |
| rdi_processor-processor.log                | RDI stream processing.                                              |
