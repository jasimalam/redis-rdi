





![data flow](/docs/images/RDIPipeDataflow.drawio.png)

**RDI Data Transformation** allows to transform and customize data as it moves from a source database into Redis. This ensures that the data is properly structured, enriched, or filtered to suit your application needs before being written to Redis.

**Key Features of RDI Data Transformation**:
- **Field Renaming** (*rename_field*): Allows renaming of specific fields from the source data without affecting other fields.
    - Example: Rename id to user_id.

- **Field Addition** (*add_field*): Adds new fields to the record, either with static values or dynamically generated expressions.
    - Example: Add a field created_at with a timestamp.

- **Field Removal** (*remove_field*): Removes unwanted fields from the data before writing it to Redis.
    - Example: Remove sensitive or unnecessary fields.

- **Filtering Records** (*filter*): Filters records based on specific criteria, allowing you to only include the data that meets certain conditions.
    - Example: Only include records where age > 18.

- **Mapping Records** (*map*): Rebuilds or remaps records using custom expressions to produce new output structures.
    - Example: Map the fields first_name and last_name into a single full_name field.

- **Custom Key Generation**: Dynamically create Redis keys using expressions like concat to define how data will be structured in Redis.
    - Example: Create a key format like user:id:12345.


### Transformation Job Example

prerequisite: [rdi configuration](/docs/rdi-configuration.md)

#### objective:

rename ***age*** column name of source db to  ***user_age*** in target redis 

source table sample

```sql
MariaDB [(none)]> SELECT * FROM testdb.sample_table;
+---------+-------------------+-----------------------------+------+-------------------------------------------------------+
| id      | name              | email                       | age  | address                                               |
+---------+-------------------+-----------------------------+------+-------------------------------------------------------+
| 1117788 | James Arthur             | james77@example.com |   58  | 381 Long Ville                                        |
```

transformation job

```bash
# cat /opt/rdi/config/jobs/job-1.yaml 
source:
  table: sample_table
transform:
  - uses: rename_field
    with:
      from_field: age
      to_field: user_age

```

apply 

```bash
# redis-di deploy --dir /opt/rdi/config --rdi-password 'REDACTED'
INFO - Reading job-1.yaml job
Deploying settings to 10.56.8.89:12001
INFO - Task `deploy` completed successfully.
```

verify 

```bash
# redis-di list-jobs  --rdi-password 'REDACTED'
Ingest Jobs
+-------+--------+----+--------+--------------+-----------------+--------+--------+-----------+
| Name  | Server | DB | Schema | Table        | Transformations | Filter | Key(s) | Target(s) |
+-------+--------+----+--------+--------------+-----------------+--------+--------+-----------+
| job-1 |        |    |        | sample_table | Yes             | No     | No     |           |
+-------+--------+----+--------+--------------+-----------------+--------+--------+-----------+

# redis-di describe-job job-1   --rdi-password 'REDACTED'
name: job-1
source:
  table: sample_table
transform:
- uses: rename_field
  with:
    from_field: age
    to_field: user_age
```

tracing the transformation 

```
# redis-di trace  --rdi-password 'REDACTED'
Starting trace for 20 second(s)
Polling records

[49e686c7-fec4-4eb4-8d1f-4f84e4d550bd] sample_table:id:1117788 2024-09-30 18:24:44.000 (+0ms) event performed in source database
[49e686c7-fec4-4eb4-8d1f-4f84e4d550bd] sample_table:id:1117788 2024-09-30 18:24:44.731 (+731ms) event received by collector
[49e686c7-fec4-4eb4-8d1f-4f84e4d550bd] Collector record: {'key': '{"id":1117788}', 'value': '{"before":null,"after":{"id":1117788,"email":"james77@example.com","age":58},"source":{"version":"2.6.1.Final","connector":"mysql","name":"rdi","ts_ms":1727699084000,"snapshot":"false","db":"testdb","sequence":null,"ts_us":1727699084000000,"ts_ns":1727699084000000000,"table":"sample_table","server_id":1,"gtid":null,"file":"mysql-bin.000009","pos":1984,"row":0,"thread":null,"query":null},"op":"c","ts_ms":1727699084731,"ts_us":1727699084731756,"ts_ns":1727699084731756000,"transaction":null}'}
[49e686c7-fec4-4eb4-8d1f-4f84e4d550bd] sample_table:id:1117788 2024-09-30 18:24:44.954 (+954ms) received OpCode.CREATE event in stream data:rdi.testdb.sample_table
[49e686c7-fec4-4eb4-8d1f-4f84e4d550bd] For sample_table:id:1117788 found transformation job: job-1
[49e686c7-fec4-4eb4-8d1f-4f84e4d550bd] sample_table:id:1117788 Before transformation:
{
  "id": 1117788,
  "email": "james77@example.com",
  "age": 58
}
[49e686c7-fec4-4eb4-8d1f-4f84e4d550bd] sample_table:id:1117788 After transformation:
{
  "id": 1117788,
  "email": "james77@example.com",
  "user_age": 58
}
```

target redis status. *age* is transformed to  *user_age*

```
127.0.0.1:18888> HGETALL sample_table:id:1117888
1) "id"
2) "1117888"
3) "email"
4) "james77@example.com"
5) "user_age"
6) "58"
```



- Other References [Link](https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/transform-examples/)
- [Parameter Reference](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/)
- [JMESPath custom function](https://redis.io/docs/latest/integrate/redis-data-integration/reference/jmespath-custom-functions/)