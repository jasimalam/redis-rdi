[!NOTE]
considering [single node installation](/docs/installation.md) is done

### Second Node

create require vm for RDI. 
download rdi binary from redis portal and transfer to vm

```bash
$ multipass launch focal -c 2 -d 15G -m 2G -n rdi-2
$ multipass transfer rdi-installation-1.2.8.tar.gz rdi-2:
$ multipass shell rdi-1
$ sudo -i
# cd /home/ubuntu/
# tar -xvf rdi-installation-1.2.8.tar.gz
# cd rdi_install/1.2.8/
```

run the install script &  use existing rdi redis database credentials

```bash
# ./install.sh
Welcome to RDI installation. This command will walk you through the installation steps.

RDI installation does not support the ability to create RDI database when:
- Cluster API is using TLS
- RDI database needs to be created using TLS

Would you like the installation to create the RDI Redis database for you? [Y/n]: n
 Please enter the RDI Redis database hostname or IP address: 10.56.8.89
Please enter the RDI Redis database port: 12001 
Please enter the RDI Redis database username to use or press enter if you are using the default user: 
Please enter the RDI Redis database password to use: [REDACTED]
Please enter the RDI Redis database password to use []:Do you want to use TLS? [y/N]: N
Testing RDI database connectivity and space...
Using existing RDI database...
Connected successfully to RDI database.

Installing RDI components. This might take a minute
....
Press select the source database type you want to use: 
1: Mysql
2: Oracle
3: Postgresql
4: Sqlserver
Select a database type by index [1]: Installation completed successfully!
```

### verify

you will find both rdi vm IP on client list


$ sudo redis-di status   --rdi-password 'REDACTED'

**Clients**
| ID          | ADDR              | Name                    | Age (sec) | Idle (sec) | User    |
|-------------|-------------------|-------------------------|-----------|------------|---------|
| 4001000     | 10.56.8.124:61071 | redis-di-operator       | 29037     | 1          | default |
| 39659001000 | 10.56.8.124:41102 | redis-di-processor      | 10772     | 0          | default |
| 61812001000 | 10.56.8.192:17571 | redis-di-subprocessor   | 64        | 64         | default |
| 61826001000 | 10.56.8.192:36887 | redis-di-monitor        | 60        | 5          | default |
| 61840001000 | 10.56.8.192:49375 | debezium:offsets        | 55        | 55         | default |
| 61943001000 | 10.56.8.192:37536 | debezium:schema_history | 11        | 11         | default |
| 2001001     | 10.56.8.124:40516 | redis-di-operator       | 29037     | 29037      | default |
| 39630001001 | 10.56.8.124:22704 | redis-di-operator       | 10785     | 1          | default |
| 39651001001 | 10.56.8.124:3249  | debezium:offsets        | 10775     | 10775      | default |
| 61827001001 | 10.56.8.192:1825  | redis-di-operator       | 59        | 59         | default |
| 61837001001 | 10.56.8.192:18242 | debezium:redis:sink     | 55        | 55         | default |
| 12001002    | 10.56.8.124:63350 | redis-di-monitor        | 29034     | 2          | default |
| 39648001002 | 10.56.8.124:61627 | debezium:redis:sink     | 10776     | 10776      | default |
| 39662001002 | 10.56.8.124:49618 | redis-di-subprocessor   | 10772     | 10772      | default |
| 39666001002 | 10.56.8.124:24521 | redis-di-processor      | 10771     | 0          | default |
| 61811001002 | 10.56.8.192:44193 | redis-di-processor      | 64        | 0          | default |
| 61815001002 | 10.56.8.192:12586 | redis-di-processor      | 63        | 3          | default |
| 61828001002 | 10.56.8.192:23822 | redis-di-operator       | 59        | 4          | default |
| 61968001002 | 10.56.8.124:38128 | redis-di-cli            | 0         | 0          | default |



