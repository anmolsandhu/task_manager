import time
import cpu_all_cores_stats
import memory_info_meminfo


def main():
	cpu_stats = cpu_all_cores_stats.cpu_cores_stats()

	for i in range(5):
		time.sleep(2)
		print cpu_stats.cpu_interval_data()
		print memory_info_meminfo.get_interval_mem_utilization()

		print "next interval"

main()