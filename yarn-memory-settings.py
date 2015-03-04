import multiprocessing
import psutil
import textwrap

CPU=psutil.cpu_count()
MEMORY=round(psutil.virtual_memory().total/1024/1024)
DISKS=7
MIN_CONTAINER_SIZE=1024


for part in psutil.disk_partitions():
    print part.device

print "%s %s %s" % (CPU,MEMORY,DISKS)
#exit

#reserved_memory=memory_for_stack+memory_for_hbase
containers=min(2*CPU,1.8*DISKS,(MEMORY/MIN_CONTAINER_SIZE))
memory_per_container=max(MIN_CONTAINER_SIZE,(MEMORY/containers))
print "Nr %s M-p_c %s" % (containers,memory_per_container)


yarn_nm_resource_mem = int(containers * memory_per_container)
yarn_sched_min    = int(memory_per_container)
yarn_sched_max    = int(containers * memory_per_container)


print "yarn.conf\n\n"
print textwrap.dedent("""
    <property>
        <name>yarn.nodemanager.resource.memory-mb</name>
        <value>%s</value>
    </property>
    <property>
        <name>yarn.scheduler.minimum-allocation-mb</name>
        <value>%s</value>
    </property>
    <property>
        <name>yarn.scheduler.maximum-allocation-mb</name>
        <value>%s</value>
    </property>""") % (yarn_nm_resource_mem,yarn_sched_min,yarn_sched_max)

'''
mapred-site.xml mapreduce.map.memory.mb = int(memory_per_container)
mapred-site.xml         mapreduce.reduce.memory.mb  = int(2 * memory_per_container)
mapred-site.xml mapreduce.map.java.opts = int(0.8 * memory_per_container)
mapred-site.xml mapreduce.reduce.java.opts  = int(0.8 * 2 * memoryper_container)

yarn-site.xml (check)   yarn.app.mapreduce.am.resource.mb   = int(2 * memory_per_container)
yarn-site.xml (check)   yarn.app.mapreduce.am.command-opts  = int(0.8 * 2 * memory_per_container)
'''
