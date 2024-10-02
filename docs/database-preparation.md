## Database Preparation

### MariaDB Setup

```bash
$ sudo apt install mariadb-server
$ sudo mysql_secure_installation
# Set root password: [REDACTED]

$ sudo sed -i 's/^bind-address\s*=\s*127\.0\.0\.1/bind-address = 0.0.0.0/' /etc/mysql/mariadb.conf.d/50-server.cnf
$ sudo systemctl restart mariadb
```

### User and Database Creation

```sql
CREATE USER 'adminuser'@'%' IDENTIFIED BY 'adminpass';
GRANT ALL PRIVILEGES ON *.* TO 'adminuser'@'%';
FLUSH PRIVILEGES;

CREATE DATABASE testdb;
CREATE USER 'rdiuser'@'%' IDENTIFIED BY 'password';
GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'rdiuser' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```

### 4.3 Binary Logging Configuration

Edit `/etc/mysql/mariadb.conf.d/50-server.cnf`:

```ini
[mysqld]
server-id = 1
log_bin = mysql-bin
binlog_format = ROW
binlog_row_image = FULL
binlog_expire_logs_seconds = 864000
binlog_annotate_row_events=ON
```

Restart and verify:

```bash
$ systemctl restart mariadb.service
```
```sql
# Verify settings
MariaDB [(none)]>  SHOW VARIABLES LIKE 'log_bin';
MariaDB [(none)]>  SHOW VARIABLES LIKE 'binlog_format';
MariaDB [(none)]> SHOW VARIABLES LIKE 'binlog_row_image';
MariaDB [(none)]>  SHOW VARIABLES LIKE 'binlog_expire_logs_seconds';
MariaDB [(none)]>  SHOW GLOBAL VARIABLES WHERE variable_name = 'binlog_row_value_options';

# If binlog_row_value_options is not blank, set it:
MariaDB [(none)]>  SET @@global.binlog_row_value_options="";
```

### 4.4 GTID Configuration

For MySQL:
```ini
[mysqld]
gtid_mode = ON
enforce-gtid-consistency = ON
```

For MariaDB:
```ini
gtid_domain_id=1
gtid_strict_mode=ON
log_slave_updates=ON
```