Configuration file: `/opt/rdi/config/config.yaml`

```yaml
targets:
  target:
    connection:
      type: redis
      host: 10.56.8.89
      port: 18888
      password: [REDACTED]
sources:
  mysql:
    type: cdc
    logging:
      level: info
    connection:
      type: mysql
      host: 10.56.8.231
      port: 3306
      database: testdb
      user: rdiuser
      password: [REDACTED]
```

Deploy the configuration:

```bash
redis-di deploy --dir /opt/rdi/config --rdi-password '[REDACTED]'
```

By default RDI ingest all tables in source database unless specified otherwise as store in target redis as hash. 

We can specify source table and column like like below

```sql
sources:
  mysql:
    type: cdc
    logging:
      level: info
    connection:
      type: mysql
      host: 10.56.8.231
      port: 3306
      database: testdb
      user: rdiuser
      password: [REDACTED]
    tables:
      testdb.sample_table:
        columns:
          - id
          - email
          - age

targets:
  target:
    connection:
      type: redis
      host: 10.56.8.89
      port: 18888
      password: [REDACTED]
```

[Reference file](/script/reference-config.yaml)
[parameter reference](https://redis.io/docs/latest/integrate/redis-data-integration/reference/config-yaml-reference/)