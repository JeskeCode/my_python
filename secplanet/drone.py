#!/usr/bin/env python

import time
import socket
import struct
import bisect
import os		

#path to directory containing drone files
drone_path = "./drone_download/"
#path to file containing partner IP range info
part_path = "vendor_long.txt"
#path for matched entry results
results_path = "drone_results.txt"
#path to error log file
err_log_path = "error.log"

try:
	#open error log for writing
	f_err = open(err_log_path,'a')

	#open results file
	f_results = open(results_path,'a')

	#temporary dictionary object
	temp_dict = {}

	#partner info list objects
	part_arr_start = []
	part_arr_end = []
	part_arr_name = []

	#iterate through partner info populating dictionary object
	for line in open(part_path,'rb'):
		#split entry into individual elements
		#starting IP, ending IP, partner name
		partnervals = line.split(',')
		#create dictionary entry
		temp_dict[int(partnervals[0])]= [int(partnervals[1]),partnervals[2]]

	#sort dictionary
	for _key in sorted(temp_dict.iterkeys()):
		part_arr_start.append(_key)
		part_arr_end.append(temp_dict[_key][0])
		part_arr_name.append(temp_dict[_key][1])

	#create list object to hold drone IP information
	drone_array = []

	#make sure path to drone files exists and is a directory
	if os.path.exists(drone_path) and os.path.isdir(drone_path) and os.access(drone_path,os.R_OK):
		#iterate through directory contents
		for _item in os.listdir(drone_path):
			#construct path to next file
			_nextfile = drone_path+_item
			#if it is a file process it
			if os.path.isfile(_nextfile) and os.access(_nextfile,os.R_OK):
				line_count = 0
				print _nextfile #iterate through file contents a line at a time
				for _line in open(_nextfile,'rb'):
					_input = ""
					_addr = 0
					line_count = line_count+1
					#skip header line
					if line_count > 1:
						#extract IP address and convert to long
						_input = _line.replace('"','').split(',')
						_addrstr =  _input[1].strip()
						try:
							_addr = struct.unpack('!L',socket.inet_aton(_addrstr))[0]
						except:
							continue
		
						#find partner info array insert point minus 1
						try:
							_entry = bisect.bisect(part_arr_start,_addr)-1	
							#if drone IP is in range of partner entry write it to results file
							if _addr >= part_arr_start[_entry] and _addr <= part_arr_end[_entry]:
								print>>f_results, '"'+part_arr_name[_entry].strip()+'",' +  _line.strip()
								#print>> str(part_arr_name[_entry].strip()) + str(',') + str(f_results)+ "," +  str(_line.strip())

						except Exception as err:
							print >>f_err, str(time.time())+" ERROR: " +err

	else: #log error with provided path to drone files
		print >>f_err, str(time.time())+" ERROR: "+drone_path+" does not exists or is not a directory"

	#close results file
	f_results.close()
	#close error log
	f_err.close()
except Exception as err:
	#close results file
	f_results.close()
	#close error log
	f_err.close()
	print "UNANTICIPATED ERROR: Unable to continue drone file processing. - "+str(err)