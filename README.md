# Server Stats


Use this script to find server details. Feel free to modify
# Installation
Fabric is best installed via pip (highly recommended) or easy_install (older, but still works fine), 
eg:

```sh
$ pip install fabric
```
You may also opt to use your operating systems package manager; the package is typically called fabric or python-fabric

eg:

```sh
$ sudo apt-get install fabric
```

Advanced users wanting to install a development version may use pip to grab the lastest master branch (as vell as the dev version of paramiko)
```sh
$ pip install paramiko==dev
$ pip install fabric==dev
```

# Quick start
# Step 1:
### Create fabric folder in your Mac or linux desktop and clone this repository

`a.git clone `
`b.Ensure fabric is installed without errors`
`c.Ensure fabfile is modified with host accessible to your environment`

Run following command 
```sh
Available commands:

    check_tcp_udp_connection_status  Sometimes server will be overwhelmed by number of open connections leading to denial of serv...
    cpu_drainer                      Used to verify process which takes more cpu
    errors_syslog                    Print any error or traces in syslog for eventual server misbehaviour
    find_largest_open_file           Used to verify largest open file which occupy disc space
    insufficient_drainer             Verify packets dropped due to memory constrain, if this increases will eventually lead to me...
    memory_drainer                   Used to verify process which takes more memory Top 5
    verify_kernel_dump               Used to verify dmesg output
```
