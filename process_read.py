


def read_file(filepath):
	f = open(filepath)

	for line in f:
		print line



read_file("/proc/378/stat")