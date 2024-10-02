## RDI Installation

create require vm for RDI. 
download rdi binary from redis portal and transfer to vm

```bash
$ multipass launch focal -c 2 -d 15G -m 2G -n rdi-1
$ multipass transfer rdi-installation-1.2.8.tar.gz rdi-1:
$ multipass shell rdi-1
$ sudo -i
# cd /home/ubuntu/
# tar -xvf rdi-installation-1.2.8.tar.gz
# cd rdi_install/1.2.8/
```

run the install script and pass required credentials

```bash
# ./install.sh
Welcome to RDI installation. This command will walk you through the installation steps.

RDI installation does not support the ability to create RDI database when:
- Cluster API is using TLS
- RDI database needs to be created using TLS

Would you like the installation to create the RDI Redis database for you? [Y/n]: Y
Please enter the Redis Enterprise Cluster hostname or IP address: 10.56.8.89
Please enter the Redis Enterprise Cluster admin API port [9443]: 
Please enter the Redis Enterprise Cluster username to use: jasim@example.com
Please enter the Redis Enterprise Cluster password to use []: [REDACTED]
Please enter the RDI Redis database username to use or press enter if you are using the default user: 
Please enter the RDI Redis database password to use: [REDACTED]
Please confirm: [REDACTED]
Would you like the RDI Redis database to be highly available (recommended for production)? [y/N]: N
Testing RDI database connectivity and space...
Creating new RDI database:
 name: redis-di-1
 port: 12001
 memory: 250MB
 shards: 1
 replication: False
New instance created on port 12001:
 DNS: redis-12001.cluster
 ADDR: 10.56.8.89
Default Context created successfully
RDI database is successfully installed and connected.

Installing RDI components. This might take a minute
......
Press select the source database type you want to use: 
1: Mysql
2: Oracle
3: Postgresql
4: Sqlserver
Select a database type by index [1]: 1
Installation completed successfully!

In order to create an RDI pipeline, please edit the /opt/rdi/config/config.yaml configuration file.
You may also add specific transformation jobs in the jobs sub-folder.

RDI needs the source & target database username and password. To set use the following:
    redis-di set-secret SOURCE_DB_USERNAME <username>
    redis-di set-secret SOURCE_DB_PASSWORD <password>
    redis-di set-secret TARGET_DB_USERNAME <username>
    redis-di set-secret TARGET_DB_PASSWORD <password>

In addition you might want to secure the connections to the source and target database
using TLS or mTLS by adding the following:
    redis-di set-secret SOURCE_DB_CACERT <path to source db CA cert>
    redis-di set-secret SOURCE_DB_CERT <path to public key pem file for the client>
    redis-di set-secret SOURCE_DB_KEY <path to private key pem file for the client>
    redis-di set-secret SOURCE_DB_KEY_PASSWORD <private key password>

    redis-di set-secret TARGET_DB_CACERT <path to target db CA cert>
    redis-di set-secret TARGET_DB_CERT <path to public key pem file for the client>
    redis-di set-secret TARGET_DB_KEY <path to private key pem file for the client>
    redis-di set-secret TARGET_DB_KEY_PASSWORD <private key password>


When you are ready, deploy your pipeline using the command:
    redis-di deploy --dir /opt/rdi/config
```