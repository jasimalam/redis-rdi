Redis Data Integration (RDI) is a powerful tool designed to help Redis Enterprise users sync their fast Redis databases with live data from slower, disk-based databases. The primary goal of RDI is to enhance the speed and scalability of read queries, ensuring a smooth and predictable user experience, especially as user demand grows.

### Key Benefits of RDI:
- **Improved Performance**: RDI caches data from read queries, enabling your application to handle millions of users without major redesigns.
- **Cost Efficiency**: By reducing the need for expensive database read replicas, RDI helps lower the total cost of ownership.
- **Simplified Operations**: RDI eliminates the need for manual pipeline building and coding data transformations, saving time and resources.

### How RDI Works:
RDI uses a Change Data Capture (CDC) mechanism to keep the Redis cache updated with changes from the primary database. It also allows you to transform data from relational tables into Redis-compatible data structures using a configuration system, eliminating the need for coding.

### Key Features:
- **Near Real-Time Updates**: RDI captures and processes changes in micro-batches, ensuring the Redis cache is almost always up to date.
- **Data Integrity**: RDI maintains the order of data changes, ensuring consistency across your database.
- **High Availability**: With hot failover and quick recovery, RDI ensures minimal downtime.
- **No Coding Required**: The system is easy to install, operate, and configure using Redis Insight and a command-line interface (CLI).
- **Security and Observability**: RDI encrypts data in transit and offers robust observability through metrics, logs, and Prometheus endpoints.
- **High Throughput**: RDI can process around 10,000 records per second, making it suitable for high-demand applications.

### When to Use RDI:
- Your app relies on a slow database as the system of record.
- You already plan to use Redis as a cache.
- Data changes frequently and can tolerate eventual consistency.

### When Not to Use RDI:
- You are migrating data into Redis only once.
- Your data is updated infrequently in large batches.
- Your app requires immediate cache consistency.
- The data set is small or you need to write data to the Redis cache first.

RDI is a solution tailored for applications that need the reliability of a disk-based database but also require the speed and scalability of Redis to handle growing user demand.