#!/usr/bin/env python3
processors = 0
with open('/proc/cpuinfo') as cpufile:
	for line in cpufile:
		if line.find('core id') != -1:
			processors += 1
print("No. of processors are : %d " %processors)

	
	
