import Tkinter as tk
from Tkinter import *
import time


#importing the cpu_all_cores_stats.py
from cpu_all_cores_stats import cpu_cores_stats

#import the memory info module
from memory_info_meminfo import Meminfo

#importing the disk stats class
from disk_stats import disk_stats_info

#importing the proc stats class
from proc_stats import get_process_info

#importing the network stats class
from network_stats import TcpUdp


class SeaofBTCapp(tk.Tk):

	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		tk.Tk.wm_title(self, "Task manager")

		

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, CpuStats, DiskStats, Process_info, NetworkStatstics):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.geometry("800x500")
		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
		if cont == CpuStats or cont == DiskStats or cont == Process_info or cont == NetworkStatstics:
			print "caling the fiunction"
			frame.update_stats()

#this is the first page as app opens

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		#title of the first window
		#self.geometry("500x500")
		

		label = tk.Label(self, text = "Start Page")
		label.pack(pady = 10, padx = 10)

		button = tk.Button(self, text = "Cpu stats", command = lambda: controller.show_frame(CpuStats))
		button.pack()

		button2 = tk.Button(self, text="Disk stats", command=lambda: controller.show_frame(DiskStats))
		button2.pack()

		button2 = tk.Button(self, text="Network stats", command=lambda: controller.show_frame(NetworkStatstics))
		button2.pack()

		button2 = tk.Button(self, text="Process_info", command=lambda: controller.show_frame(Process_info))
		button2.pack()

		# button3 = tk.Button(self, text = "visit page 3")
		# button3.pack()


class CpuStats(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		print "CpuStats  ", self
		label = tk.Label(self, text="CPU STATS!!!")
		label.pack(pady=10,padx=10)

		button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
		#button1.grid(row = 0, column = 1)
		button1.pack()



		self.listbox = tk.Listbox(self)
		self.listbox.insert(0, "CPU     user    system   overall      intr     cntxt    memutil   totalmem    avalmem")
		self.listbox.itemconfig(0, {'bg':'red'})
		self.listbox.insert(1, "anmoldeep")
		self.listbox.insert(2, "anmoldeep")
		self.listbox.insert(3, "anmoldeep")
		self.listbox.pack(side = BOTTOM, fill = BOTH)

		
		self.time = 0
		self.count = 0

		#initializing the class all_core_stats
		self.cpu_stats = cpu_cores_stats()

		#innitoializing the meminfo class
		self.mem_stats = Meminfo()		

	def clear_listbox(self):
		self.listbox.delete(1, END)

	def fill_listbox(self, cpu_stats):
		count = 1
		for data in cpu_stats:
			self.listbox.insert(count, data)
			count += 1


	def update_stats(self):
		cpu_stats = self.get_cpu_label_box_output_val()
		self.clear_listbox()
		self.fill_listbox(cpu_stats)
		self.listbox.after(self.time + 1000, self.update_stats)

	
	def get_cpu_label_box_output_val(self):
		cpu_data = self.get_cpu_mem_stats()
		
		cpu =  "cpu " + "    "  +"%.2f" % cpu_data[0][0] + "    "  \
				+ "%.2f" % cpu_data[0][1] +  "    " + "%.2f" % cpu_data[0][2] +  "          " \
				+ "%d" % cpu_data[0][3] + "    " +  "%d" % cpu_data[0][4] + "    "\
				+ "%.2f" % cpu_data[5] + "     " +"%.2f" % cpu_data[6] + "      " +"%.2f" % cpu_data[7]

		cpu0 = "cpu0" + "    "+ "%.2f" % cpu_data[1][0] + "    " + "%.2f" % cpu_data[1][1] +  "    " + "%.2f" % cpu_data[1][2]
		cpu1 = "cpu1" + "    "+ "%.2f" % cpu_data[2][0] + "    " + "%.2f" % cpu_data[2][1] +  "    " + "%.2f" % cpu_data[2][2]
		cpu2 = "cpu2" + "    "+ "%.2f" % cpu_data[3][0] + "    " + "%.2f" % cpu_data[3][1] +  "    " + "%.2f" % cpu_data[3][2]
		cpu3 = "cpu3" + "    "+ "%.2f" % cpu_data[4][0] + "    " + "%.2f" % cpu_data[4][1] +  "    " + "%.2f" % cpu_data[4][2]
		
		return [cpu, cpu0, cpu1, cpu2, cpu3]

		

	def get_cpu_mem_stats(self):
		cpu_data = self.cpu_stats.cpu_interval_data() 
		mem_data = self.mem_stats.get_mem_info()
		#print cpu_data
		cpu = cpu_data['cpu']
		cpu0 = cpu_data['cpu0']
		cpu1 = cpu_data['cpu1']
		cpu2 = cpu_data['cpu2']
		cpu3 = cpu_data['cpu3']
		cpu.append(cpu_data['intr'])
		cpu.append(cpu_data['ctxt'])

		#print mem_data
		avg_mem_avaliable = mem_data['avg_mem_avaliable']
		avg_mem_total = mem_data['avg_mem_total']
		avg_mem_utilization = mem_data['avg_mem_utilization']


		return [cpu, cpu0, cpu1, cpu2, cpu3, avg_mem_utilization, avg_mem_total, avg_mem_avaliable]


class DiskStats(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Disk stats")
		label.pack(pady=10,padx=10)

		button1 = tk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		button1.pack()

		self.listbox = tk.Listbox(self)
		self.listbox.insert(0, "disk_r     disksecread    disk_w     disksecwritten")
		self.listbox.itemconfig(0, {'bg':'red'})
		self.listbox.pack(side = BOTTOM, fill = BOTH)


		#initialize the diskinfo class
		self.disk_stats = disk_stats_info()

		#self time 
		self.time = 0

		#just a test val
		self.count = 0


	def clear_listbox(self):
		self.listbox.delete(1, END)


	def fill_listbox(self, disk_stats):
		self.listbox.insert(1, disk_stats)
			

	def update_stats(self):
		disk_stats = self.get_disk_labelbox_input()
		self.clear_listbox()
		self.fill_listbox(disk_stats)
		self.listbox.after(self.time + 1000, self.update_stats)


	def get_disk_labelbox_input(self):
		disk_stats = self.get_disk_stats()
		disk_reads = str(disk_stats['disk_reads_interval'])
		disk_sectors_read = str(disk_stats['disk_sectors_read_interval'])
		disk_writes = str(disk_stats['disk_writes_interval'])
		disk_sectors_written = str(disk_stats['disk_sectors_written_interval'])
	
		label_output = disk_reads + "            "	+ disk_sectors_read + "            " + disk_writes + "            "	 + disk_sectors_written
		return label_output	

	def get_disk_stats(self):
		disk_stats = self.disk_stats.get_disk_info()
		#print disk_stats
		return disk_stats

class NetworkStatstics(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Network stats")
		label.pack(pady=10,padx=10)

		button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
		
		button1.pack()

		self.listbox = tk.Listbox(self)
		self.listbox.insert(0, "disk_r     disksecread    disk_w     disksecwritten")
		self.listbox.itemconfig(0, {'bg':'red'})
		self.listbox.pack(side = BOTTOM, fill = BOTH)

		#intializing the network stats
		self.net_stats = TcpUdp()

		self.time = 0


		def clear_listbox(self):
			self.listbox.delete(1, END)


		def fill_listbox(self, disk_stats):
			self.listbox.insert(1, disk_stats)
			

		def update_stats(self):
			disk_stats = self.get_network_labelbox_input()
			self.clear_listbox()
			self.fill_listbox(disk_stats)
			self.listbox.after(self.time + 1000, self.update_stats)

		def get_network_labelbox_input(self):
			tcp_udp_con =  self.net_stats.get_active_tcp_conncetions()

			for conn in tcp_udp_con:
				print tcp_udp_con

class Process_info(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Process_info")
		label.pack(pady=10,padx=10)

		button1 = tk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		button1.pack()

		self.listbox = tk.Listbox(self)
		self.listbox.insert(0, "procid     procname     username   usertime     systemtime    virtualmem   resmemory")
		self.listbox.itemconfig(0, {'bg':'red'})
		self.listbox.pack(side = BOTTOM, fill = BOTH)


		self.time = 0

		#initialize the process class 
		self.process_info = get_process_info()

	def clear_listbox(self):
		self.listbox.delete(1, END)

	def fill_listbox(self, proc_info):
		count = 1
		for data in proc_info:
			self.listbox.insert(count, data)
			count += 1

	def update_stats(self):
		process_stats = self.get_process_label_box_input()
		self.clear_listbox()
		self.fill_listbox(process_stats)
		self.listbox.after(self.time + 1000, self.update_stats)

	def get_process_label_box_input(self):
		process_stats = self.process_info.get_processes_stats_interval()

		label_box_output = []
		for process in process_stats:
			stat_row = str(process[0]) + "     " +  str(process[1])  + "     " + str(process[2])  + "     " + str(process[3])  + "     " +  str(process[4])  + "     " +  str(process[5]) + "     " + str(process[6]) 
			label_box_output.append(stat_row)

		return label_box_output  


app = SeaofBTCapp()
app.mainloop()






