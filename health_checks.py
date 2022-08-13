#!/usr/bin/env python3

import os
import shutil
import sys
import socket
import psutil

def check_reboot():
    """Returns True if computer has a pending reboot"""
    return os.path.exists("/run/reboot-require")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise"""
    du = shutil.disk_usage(disk)
    # Calculate the % of free space
    percent_free = 100 * du.free / du.total
    # Calculare free gigabytes
    gb_free = du.free / 2**30
    if percent_free < min_percent or gb_free < min_gb:
        return True
    return False
def check_root_full():
	"""Returns True if the root directory is full, False otherwise"""
	return check_disk_full(disk="/",min_gb=2,min_percent=10)

def check_cpu_constrained():
	"""Returns True if the cpu is having too much usage, False otherwise"""
	return psutil.cpu_percent(1) > 75

def check_no_network():
	"""Returns True if it fails to resolve Google's URL, False otherwise"""
	try:
		socket.gethostbyname("www.google.com")
		return False
	except:
		return True

def main():
	checks = [
		(check_reboot,"Pending reboot"),
		(check_root_full,"Root partion is full"),
		(check_cpu_constrained,"CPU load too high."),
		(check_no_network,"No network is available"),
	]
	everything_ok = True
	

	for check,msg in checks:
		if check():
			print(msg)
			sys.exit(1)
	if not everything_ok:
		sys.exit(1)
	print("Everything ok.")
main()
