## Verification

Below is to test wether data ingestion is working or not.



### Data Generation

I have used this python [script](/script/db-random-data-insert.py) for data insert in  db.

```bash
# python3 random-data-insert.py 
Enter the total number of records to insert: 100
Connected to MariaDB
Table 'sample_table' created or already exists.
Inserted 100 records.
MariaDB connection closed.
```

similar script of data [update](/script/db-random-data-update.py) and [delete](/script/db-random-data-delete.py) on source DB.  

### Verify from DB

```sql
MariaDB [(none)]> SELECT COUNT(*) AS total_records
    -> FROM testdb.sample_table;
+---------------+
| total_records |
+---------------+
|           100 |
+---------------+
1 row in set (0.001 sec)
```



### Verify from Target Redis

```
> info keyspace
# Keyspace
db0:keys=100,expires=0,avg_ttl=0
```



### verify from RDI status

```bash
# redis-di status --rdi-password 'REDACTED'
```

#### Ingested Data Streams

| Name                         | Total     | Pending | Inserted  | Updated | Deleted   | Filtered | Rejected | Deduplicated | Last Arrival             |
|------------------------------|-----------|---------|-----------|---------|-----------|----------|----------|--------------|--------------------------|
| data:rdi.testdb.sample_table  | 100 | 0       | 100 | 100   | 0 | 0        | 0        | 0            | 25 Sep 2024 16:10:57.743 |


#### Performance

| Measurement             | Batch Size (records) | Records/sec | Total Time (ms) | Read Time (ms) | Process Time (ms) | Ack Time (ms) |
|-------------------------|----------------------|-------------|-----------------|----------------|-------------------|---------------|
| Last batch              | 100                  | 915         | 109             | 100            | 9                 | 1             |
| Last 1 batches (Avg) | 100                  | 915         | 109             | 100            | 9                 | 1 |


same can be done from redis cloud insight also. 
