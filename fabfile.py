#!/usr/bin/python2.7
from fabric.api import *
from fabric import decorators
from fabric.state import env
env.use_ssh_config = True
from fabric.decorators import roles,tasks

env.roledefs.update({
    'server_set1' : ['<server1>','<server2>','<server3>'],
    'server_set2' : ['<server4>','<server5>','<server6>']

})

@task
@roles('server_set1','server_set2')

def verify_kernel_dump():
  ''' Used to verify dmesg output'''
  #env.hosts = ['localhost']
  kernel_dump = run("dmesg")

  print "Check 1: Verify dmesg for segfaults and Errors", env.hosts
  if "segfault" in kernel_dump.lower() or "error" in kernel_dump.lower() or "warning" in kernel_dump.lower():
      print "Error Found in kernel boot",kernel_dump
  else :
      pass

@task
@roles('server_set1','server_set2')
def find_largest_open_file():
  ''' Used to verify largest open file which occupy disc space '''
  list_files = run("lsof | grep REG | awk '{print $1,$7,$9}' |sort -t ' ' -k 2 -V | tail 5")
  print " Check 2: Print the largest file open in host: %s and files: %s" %(host.env,list_files)
  
  


@task
@roles('server_set1','server_set2')
def cpu_drainer():
  ''' Used to verify process which takes more cpu '''
  cpu_max = run("ps aux |sort -nrk 3,3| head -5 | awk {'print $3'}")
  print " Check 3: Print most cpu hungry process : %s and files: %s" %(host.env,cpu_max) 
  
@task
@roles('server_set1','server_set2')
def memory_drainer():
  ''' Used to verify process which takes more memory Top 5 '''
  memory_max = run("ps aux |sort -nrk 3,3| head -5 | awk {'print $4'}")
  print " Check 4: Print most memory hungry process : %s and files: %s" %(host.env,memory_max) 
  

@task
@roles('server_set1','server_set2')
def insufficient_drainer():
  ''' Verify packets dropped due to memory constrain, if this increases will eventually lead to memory leak/corruption '''
  insufficient = run("netstat -s |grep -i \"insufficient memory\" ")
  print " Check 5: Print if memory is not available to handle packets : %s and files: %s" %(host.env,insufficient) 
  
  
  
@task
@roles('server_set1','server_set2')
def errors_syslog():
  ''' Print any error or traces in syslog for eventual server misbehaviour '''
  syslog_error = run("cat /var/log/*.log |egrep -i \"warning|error|alarm|fail\"")
  print " Check 6: Print any syslog mys : %s and syslog error: %s" %(host.env,syslog_error) 
  
  
  
@task
@roles('server_set1','server_set2')
def check_tcp_udp_connection_status():
  ''' Sometimes server will be overwhelmed by number of open connections leading to denial of service '''
  connections = run("netstat -ant |awk {'print $6'}| sort |uniq -c |sort -n")
  print " Check 6: Print open connection entry in  : %s and syslog error: %s" %(host.env,connection) 
  
  
    


