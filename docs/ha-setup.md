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

