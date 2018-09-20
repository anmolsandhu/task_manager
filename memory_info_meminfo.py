import time

meminfo_file = '/proc/meminfo'

kb_per_mb = 1024


class Meminfo():

	def __init__(self):
		self.prev_mem_total, self.prev_mem_available = self.get_current_mem_info()
		# print "hello"
		# print self.prev_mem_total
		# print self.prev_mem_available


	def get_current_mem_info(self):

		#openign meminfo file
		fp = open(meminfo_file)

		#
		lines = []
		for line in fp:
			lines.append(line.split())

		#print lines

		mem_info = []
		mem_info.append((int(lines[0][1])) / float(kb_per_mb)) 
		mem_info.append(int(lines[2][1]) / float(kb_per_mb))
		#mem_info.append(((mem_info[0] - mem_info[1]) / mem_info[0] ) * 100)

		#print mem_info
		return mem_info

	def get_mem_info(self):

		current_mem_total, current_mem_available  = self.get_current_mem_info()
		
		mem_stats = self.calculate_avg_mem_info(current_mem_total, current_mem_available)

		self.prev_mem_total = current_mem_total
		self.prev_mem_available = current_mem_available

		return mem_stats

	def calculate_avg_mem_info(self, current_mem_total, current_mem_available):

		avg_mem_total = (current_mem_total + self.prev_mem_total) / 2
		avg_mem_avaliable = (current_mem_available + self.prev_mem_available) / 2
		avg_mem_utilization = ((avg_mem_total - avg_mem_avaliable) / avg_mem_total) * 100

		mem_stats = {}
		mem_stats['avg_mem_total'] = avg_mem_total
		mem_stats['avg_mem_avaliable'] = avg_mem_avaliable
		mem_stats['avg_mem_utilization'] = avg_mem_utilization

		return mem_stats


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
	#print  get_interval_mem_utilization()
	a = Meminfo()
	for i in range(4):
		time.sleep(3)
		print a.get_mem_info()






