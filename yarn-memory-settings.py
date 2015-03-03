import multiprocessing
import psutil

CPU=psutil.cpu_count()
MEMORY=round(psutil.virtual_memory().total/1024/1024)
DISKS=7
MIN_COINTAINER_SIZE=1024

print "%s %s %s" % (CPU,MEMORY,DISKS)
#exit

#reserved_memory=memory_for_stack+memory_for_hbase
nr_of_cointainers=min(2*CPU,1.8*DISKS,(MEMORY/MIN_COINTAINER_SIZE))
memory_per_cointainer=max(MIN_COINTAINER_SIZE,(MEMORY/nr_of_cointainers))
print "Nr %s M-p_c %s" % (nr_of_cointainers,memory_per_cointainer)
