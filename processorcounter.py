#!/usr/bin/env python3
processors = 0
with open('/proc/cpuinfo') as cpufile:
	for line in cpufile:
		if line.find('cpu cores') != -1 :
			processors += int(line[line.find(':')+2::])

print("No. of processors are : %d " %processors)

	
	
