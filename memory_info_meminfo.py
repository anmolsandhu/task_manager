

meminfo_file = '/proc/meminfo'

kb_per_mb = 1024

def get_interval_mem_utilization():

	fp = open(meminfo_file)

	lines = []
	count = 0
	for line in fp:
		lines.append(line.split())
		if count == 3:
			break

	mem_info = {}
	mem_info['mem_total'] = (int(lines[0][1])) / float(kb_per_mb) 
	mem_info['mem_available'] = int(lines[2][1]) / float(kb_per_mb)
	mem_info['mem_utilizaion'] = ((mem_info['mem_total'] - mem_info['mem_available']) / mem_info['mem_total'] ) * 100 

	return mem_info

if __name__ == '__main__':
	print  get_interval_mem_utilization()






