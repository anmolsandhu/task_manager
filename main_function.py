import time
import cpu_all_cores_stats
from memory_info_meminfo import Meminfo
from disk_stats import disk_stats_info

def main():
	cpu_stats = cpu_all_cores_stats.cpu_cores_stats()
	mem_info = Meminfo()
	disk_info = disk_stats_info()
	for i in range(5):
		time.sleep(2)
		print cpu_stats.cpu_interval_data()
		print mem_info.get_mem_info()
		print disk_info.get_disk_info()
		print "next interval"
main()