import os
import time

# getting the process stats
proc_path = '/proc'
uptime_file = '/proc/uptime'
cpu_stat_file = '/proc/stat'

class get_process_info():

	def __init__(self):
		self.prev_cpu_idle_time = self.get_cpu_idle_time()
		self.prev_process_stats = self.get_process_data()


	def get_processes_stats_interval(self):

		current_stats = self.get_process_data()

		process_interval_stats = self.calculate_stats(current_stats)
		
		# test code
		# for p in process_interval_stats:
		# 	if p[7] > 0:
		# 		print p

		sorted_process_stats = self.sort_the_proc(process_interval_stats)

		print sorted_process_stats

		#setting the current to prev stats
		self.prev_process_stats = current_stats

		#self.idle time is changed in calculate_stats
		self.prev_cpu_idle_time = self.get_cpu_idle_time()

	def sort_the_proc(self, process_interval_stats):

		d = sorted(process_interval_stats, reverse = True, key = lambda x:x[7])
		return d

	def calculate_stats(self, current_stats):

		#constants
		process_id_position = 0
		user_time_position = 3
		sys_time_position = 4

		all_process_stats = []
		for curr_process in current_stats:
			check = self.process_last_active(curr_process[process_id_position])
			if check[0]:
				process_stats = []
				prev_process = check[1]

				#calculating all stats 
				current_cpu_idle_time = self.get_cpu_idle_time()
				idle_interval_time = current_cpu_idle_time - self.prev_cpu_idle_time

				#setting old cpu time interval
				
				usr_time_interval =  curr_process[user_time_position] - prev_process[user_time_position]
				sys_time_interval =  curr_process[sys_time_position] - prev_process[sys_time_position]

				total_time = usr_time_interval + sys_time_interval + idle_interval_time

				usr_utilization = (usr_time_interval / float(total_time)) * 100
				sys_utilization = (sys_time_interval / float(total_time)) * 100
				overall_utilization = ((usr_time_interval + sys_time_interval)  / float(total_time)) * 100

				process_stats.append(curr_process[0]) # process id  0
				process_stats.append(curr_process[1]) # program name 1
				process_stats.append(curr_process[2]) # effective_user_ id 2
				process_stats.append(curr_process[5]) # virtual memory total 3
				process_stats.append(curr_process[6]) # res memory size 4
				process_stats.append(usr_utilization) # usr utilization 5
				process_stats.append(sys_utilization) #sys utilization 6
				process_stats.append(overall_utilization) #overall utilization 7

				all_process_stats.append(process_stats)


		return all_process_stats



	def process_last_active(self, process_id):

		flag = False
		proc = None
		for process in self.prev_process_stats:
			if process_id == process[0]:
				flag = True
				proc = process
				break

		return [flag, proc]
	
	def get_process_data(self):

		self.process = get_process_paths("stat")

		process_stats = []
		for file_path in self.process:
			fp = open(file_path)
			process_stats.append(self.get_process_stats(fp))
		
		#print process_stats
		return process_stats

	def get_cpu_idle_time(self):

		fp = open(cpu_stat_file)
		line = fp.readline().split()
		return int(line[4])


	def get_process_stats(self, fp):

		line = fp.readline().split()
		#print line
		stats = []
		stats.append(int(line[0])) #process id        0
		stats.append(line[1][1:-1])	#program name     1
		stats.append(int(line[3]))	#effective user id     2
		stats.append(int(line[14])) #user time in jiffies   3
		stats.append(int(line[15])) #system time in jiffies   4
		stats.append(int(line[23])) #virtual memory size of process   5
		stats.append(int(line[24])) #resident memory size   6

		#print stats
		return stats


def get_processes(folder):

	dir_list = os.listdir(folder)

	process_dir = []
	for  dir_name in dir_list:
		try:
			dn = int(dir_name)
			process_dir.append(dir_name)
		except Exception, e:
			pass

	return process_dir


#given folder name and process list return the path to 
# the process_folder within the process_list
def get_process_paths(process_folder):

	process_list = get_processes(proc_path)
	folder_names = []
	for dir_name in process_list:
		fp = '/proc/'+ dir_name + "/" + process_folder
		folder_names.append(fp)

	return folder_names

#get_process_paths("stat")



if __name__ == "__main__":
	a = get_process_info()
	for i in range(5):
		time.sleep(2)
		a.get_processes_stats_interval()
























